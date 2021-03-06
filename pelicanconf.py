#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Simon Walker'
SITENAME = 'circularspace'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL Structure
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Menu items
MENUITEMS = [('all', '/archives.html'), ]

# Theming
THEME = 'themes/pelican-clean-blog'
HEADER_COVER = None
HEADER_COLOR = '#444'
BOOTSTRAP_THEME = 'readable'
PYGMENTS_STYLE = 'monokai'
BOOTSTRAP_FLUID = True

# Blogroll
LINKS = (('CV', 'https://mindriot101.github.io/cv/'),
        ('Work', 'https://www2.warwick.ac.uk/fac/sci/physics/research/astro/people/walker/')
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/srwalker101'),
          ('github', 'https://github.com/mindriot101'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Copy CNAME file to output
STATIC_PATHS = ['extra/CNAME', 'extra/keybase.txt', 'images']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/keybase.txt': {'path': 'keybase.txt'},
}

USE_PAGER = True

GITHUB_URL = 'https://github.com/mindriot101'
TWITTER_URL = 'https://twitter.com/srwalker101'
COLOR_SCHEME_CSS = 'monokai.css'
