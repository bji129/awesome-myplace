#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brandon Ji'
SITENAME = '德泽 vs. 德馨'
SITEURL = 'https://www.jideze.com'
TIMEZONE = 'Asia/Shanghai'

PATH = 'content'


DEFAULT_LANG = 'zh-cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Blog-pelican', 'http://getpelican.com/'),
         ('Mermaid', 'https://mermaid.live/'),
         ('UML IO', 'https://draw.io/'),
         ('QFL Courses', 'http://www.jideze.com/others/QFL-13.html'),
         ('Data Table', 'https://datatables.net/'),
         ('Linkedin', 'https://cn.linkedin.com/in/bji129')
)

# Social widget
SOCIAL = (('Github', 'http://github.com/bji129'),
         ('AboutMe', 'https://about.me/brandon.ji'),
         )

DEFAULT_PAGINATION = 4

THEME = 'themes/brandon'

# FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True