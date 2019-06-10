from markdown import Markdown
from datetime import datetime, timedelta
import mkdcomments
comments = mkdcomments.CommentsExtension()
from fontawesome_markdown import FontAwesomeExtension
from markdown.extensions.toc import TocExtension
import re, os, sys, operator, pprint, dateutil.parser
from statipy import search_parents

#Custom Markdown Jinja2 filters
markdown = Markdown(extensions=[
	'markdown.extensions.extra',
	'markdown.extensions.codehilite',
	'markdown.extensions.smarty',
	TocExtension(title='Table of Contents')
])

def includefile(filename, *args):
	return open(filename).read()


def includemd(filename, *args):
	"""Use with {{ myfile.md | includemd }}"""
	f = search_parents('.', filename)
	markdown.reset()
	m = markdown.convert(open(f).read())
	return m


def md(content, *args):
	"""Use with
	{% filter md %}
		#Header
	{% endfilter %}
	(Note that whitespace will be removed from the beginning of lines
	according to the first line, so indentation can be preserved.)
	"""
	ws = re.match(r'\s*', content.splitlines()[0]).group(0)
	c = re.compile('^%s' % ws, re.MULTILINE).sub('', content)
	markdown.reset()
	return markdown.convert(c)


def sortby(items, attribute, sortlist):
	"""Use with {{ list | sortby(attribute, sortlist) }}
	where attribute is the attribute of each item in the list to sort by
	and sortlist is a list of possible values of that attribute sort, in
	the order for them to be sorted by."""
	ag = lambda a: a.get(attribute).lower()
	sl = [s.lower() for s in sortlist]
	return sorted(items, key=lambda x:(
		sl.index(ag(x)) if ag(x) in sl else len(sl)+1, x.get('title', '')))


def dictsortby(items, attribute, sortlist):
	"""Same as sortby but with a list of dicts."""
	ag = lambda a: a[attribute].lower().replace('_', ' ')
	sl = [s.lower().replace('_', ' ') for s in sortlist]
	return sorted(items, key=lambda x:(sl.index(ag(x)) if ag(x) in sl
			else len(sl)+1, x['title']))


def ago(dto, *args):
	"""Return the number of seconds ago the passed datetime object
	was."""
	return (datetime.now() - dto).total_seconds()


def split(string, splitter, flags=re.M):
	return [s.strip() for s in re.split(splitter, string, flags=flags)]
	return [s.strip() for s in string.split(splitter)]


def nicedate(d, fmt='%B %-d, %Y'):
	return d.strftime(fmt)


def rmext(s):
	"""Remove the extension from a string"""
	return os.path.splitext(s)[0]


def debug(s):
	"""Debug to the console. Use like {{'message' | debug}}"""
	print s
	return ''


def date_table_from_file(filename, fmt='%b %d'):
	"""Read a csv file and create a date table from it. The first column
	of the first row should contain the start date and the second column
	of the first row the word "days" or "weeks". Add "rel" to the end of
	this to have each row be relative to the previous. Each subsequent row
	should contain the number of days or weeks as specified in the first
	column, and the actual text for the table in the second column
	(renderable as Markdown)."""
	r = ['<table class="table">']
	import csv
	f = csv.reader(open(filename))
	start, step = f.next()
	start = dateutil.parser.parse(start)
	for rv, val in f:
		markdown.reset()
		rv = float(rv) * (7 if step == 'weeks' else 1)
		r.append('<tr><td>{}</td><td>{}</td>'.format(
			start + timedelta(days=rv), markdown.convert(val)
		))
	return '\n'.join(r)


JINJA_EXTENSIONS = ['jinja2.ext.do']

JINJA_FILTERS = {
	'includefile': includefile,
	'includemd':   includemd,
	'md':          md,
	'sortby':      sortby,
	'dictsortby':  dictsortby,
	'ago':         ago,
	'type':        type,
	'split':       split,
	'nicedate':    nicedate,
	'rmext':       rmext,
	'debug':       debug,
}


options = {
	'jinja2_filters':    JINJA_FILTERS,
	'jinja2_extensions': JINJA_EXTENSIONS,
}
