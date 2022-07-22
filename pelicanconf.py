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
LINKS = (('博客工具', 'http://getpelican.com/'),
         ('在线编辑', 'https://mermaid.live/'),
         ('UML画图', 'https://draw.io/'),
         ('七外课程表', 'http://www.jideze.com/others/QFL-13.html'),
         ('动态数据表', 'https://datatables.net/'),
         ('联系我', 'https://about.me/brandon.ji'),
         ('个人资料', 'https://cn.linkedin.com/in/bji129')
)

# Social widget
SOCIAL = (('代码库', 'http://github.com/bji129'),)

DEFAULT_PAGINATION = 4

THEME = 'Chunk'

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True