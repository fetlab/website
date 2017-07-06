#!/usr/bin/env python

import subprocess, os, shutil, re, cPickle, sys, time, bibtexparser
from colortext import colortext
from operator import itemgetter

formats = {
'inproceedings':
"""
<div class="publicationitem">
	<div class="publication">
		<span class="year">{year}</span>
		<span class="authors">{authors}</span>.
		<span class="title">{title}</span>.
		In <span class="pubvenue"><span class="booktitle">{booktitle},</span>
		<span class="pagenums">pp. {pages}</span></span>.
		<a href="/{catroot}/{pdffile}"><span class="fa fa-file-pdf-o"></span></a>
	</div>
</div>
""",
'article':
"""
<div class="publicationitem">
	<div class="publication">
		<span class="year">{year}</span>
		<span class="authors">{authors}</span>.
		<span class="title">{title}</span>.
		<span class="pubvenue"><span class="journal">{journal},</span>
		<span class="volume">{volume}</span><span class="number">({number}),</span>
		<span class="pagenums">pp. {pages}</span></span>.
		<a href="/{catroot}/{pdffile}"><span class="fa fa-file-pdf-o"></span></a>
	</div>
</div>
""",
}

def fixauthors(authors):
	return [' '.join(author.split(', ')[::-1]) for author in authors.split(' and ')]


def bibentry2html(e):
	authors = fixauthors(e['author'])
	if len(authors) > 2:
		e['authors'] = ', '.join(authors[:-1]) + ' and {0}'.format(authors[-1])
	elif len(authors) == 2:
		e['authors'] = ' and '.join(authors)
	else:
		e['authors'] = authors
	return formats[e['ENTRYTYPE']].format(**e)


global _debug
_debug = False

def get_papers(proxy_strip=''):
	script = """
	set z to ""
	tell application "Papers"
		repeat with p in (selected publications of front library window as list)
			if p's primary file item is not missing value then
				set b to bibtex string of p as text
				set b2 to characters 1 thru -5 of b
				set u to my remove_text(the publication url of p, "{proxy_strip}")
				set b2 to (b2 & ",\nurl = {" & u & "},\nfilename = {" & the full path of the primary file item of p as text) & "}\n}"
				set z to z & "\n\n" & b2
			end if
		end repeat
	end tell
	return z

	on remove_text(this_text, text_to_rm)
		set AppleScript's text item delimiters to text_to_rm
		set the item_list to every text item of this_text
		set AppleScript's text item delimiters to ""
		set this_text to the item_list as string
		return this_text
	end remove_text
""".format(proxy_strip=proxy_strip)

	osa = subprocess.Popen(['osascript', '-'],
												 stdin=subprocess.PIPE,
												 stdout=subprocess.PIPE,
												 stderr=subprocess.PIPE)
	o,e = osa.communicate(script)

	if e:
		raise IOError("ERROR: %s" % e)

	return o

def gen_pubs(dest):
	#Load and sort pubs
	for p in bibtexparser.loads(get_papers()).entries:
		fnbase = p['year'] + '-' + p['title'].replace(': ', '-').replace('/', '_')
		print fnbase
		subprocess.check_call(['convert', '-resize', 'x200',
			'-background', 'white', '-alpha', 'remove', '-unsharp', '0x1',
			'%s[0]' % p['filename'], os.path.join(dest, '%s.png' % fnbase)])
		shutil.copy(p['filename'], os.path.join(dest, '%s.pdf' % fnbase))
		p['thumbimg'] = '%s.png' % fnbase
		p['pdffile']  = '%s.pdf' % fnbase
		p['catroot']  = 'publications'
		with open(os.path.join(dest, '%s.md' % fnbase), 'w') as f:
			f.write('Title: {title}\nDate: {year}-01-01\nImage: {thumbimg}\n'.format(**p))
			f.write(bibentry2html(p))

if __name__ == "__main__":
	gen_pubs('content/publications')
