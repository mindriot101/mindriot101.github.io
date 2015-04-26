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
THEME = 'themes/notmyidea'

# Blogroll
LINKS = (('CV', 'http://mindriot101.github.io/cv/'),
        ('Work', 'http://www2.warwick.ac.uk/fac/sci/physics/research/astro/people/walker/')
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/srwalker101'),
          ('github', 'https://github.com/mindriot101'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
