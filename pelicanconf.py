#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from markdown import Markdown
import mkdcomments
import re, os, sys

AUTHOR       = u'Daniel Ashbrook'
SITENAME     = AUTHOR
SITEURL      = ''
TIMEZONE     = 'EST'
DEFAULT_LANG = u'en'

FILENAME_METADATA = '(?P<fname>.*)'

PATH = 'content'
PAGE_URL = '{category}/{fname}.html'
PAGE_SAVE_AS = PAGE_URL
PAGE_PATHS = ['pages']
STATIC_PATHS = ['js', 'css', 'fonts', 'images', 'misc', 'files',
	'font-awesome']
ARTICLE_EXCLUDES = STATIC_PATHS
PAGE_EXCLUDES = ARTICLE_EXCLUDES
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'smartypants',
	'toc(title=Table of Contents)']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme'


#Custom Markdown Jinja2 filters
markdown = Markdown(extensions=['markdown.extensions.extra',
	'markdown.extensions.codehilite', mkdcomments.CommentsExtension()])

def includefile(filename, *args):
	print "includefile(%s)" % os.path.join(os.getcwd(), filename)
	return open(filename).read()

def includemd(filename, *args):
	"""Use with {{ myfile.md | includemd }}"""
	print "includemd(%s)" % os.path.join(os.getcwd(),filename)
	m = markdown.convert(open(filename).read())
	open('/tmp/mdout', 'w').write(m)
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
	return markdown.convert(c)

JINJA_FILTERS = {
	'includefile': includefile,
	'includemd': includemd,
	'md':        md,
}
