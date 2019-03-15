try:
	from StringIO import StringIO
except ImportError:
	from io import StringIO
from pybtex.database.input.bibtex import Parser
from pybtex.database.output.bibtex import Writer
from pybtex.database import BibliographyData, PybtexError
from pybtex.backends import html
from pybtex.style.formatting import plain

def do_bibtex(bibfile):
	plain_style = plain.Style()
	bibdata_all = Parser().parse_file(bibfile)
	html_backend = html.Backend()
	formatted_entries = plain_style.format_entries(bibdata_all.entries.values())

	publications = []
	publications_lists = {}
	publications_untagged = []

	for formatted_entry in formatted_entries:
		key    = formatted_entry.key
		entry  = bibdata_all.entries[key]
		year   = int(entry.fields.get('year'))
		url    = entry.fields.get('url', None)
		slides = entry.fields.get('slides', None)
		poster = entry.fields.get('poster', None)

		#render the bibtex string for the entry
		bib_buf = StringIO()
		bibdata_this = BibliographyData(entries={key: entry})
		Writer().write_stream(bibdata_this, bib_buf)
		text = formatted_entry.text.render(html_backend)

		entry_tuple = {\
			'key':    key,
			'year':   year,
			'text':   text,
			'bibtex': bib_buf.getvalue(),
			'url':    url,
			'slides': slides,
			'poster': poster,
			'entry':  entry,}

		publications.append(entry_tuple)

	return publications
