#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.simonrw.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.xml'
TAG_FEED_ATOM = 'feeds/tag_%s.xml'

DELETE_OUTPUT_DIRECTORY = True
