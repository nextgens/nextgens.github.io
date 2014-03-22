#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Florent Daigni\xe8re'
SITENAME = u"NextGen$'s blog"
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None

FEED_DOMAIN = 'http://florent.daigniere.com/'
FEED_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DEFAULT_DATE_FORMAT = ('%d %b, %Y')
AUTHOR_BIO = 'The blog of an opiniated french guy, Technical Director (<a href="https://www.trustmatta.com/">@Matta</a>), BOFH and core developer (<a href="https://freenetproject.org">@Freenet</a>), traveller, hacker.'

# Social widget
TWITTER_USERNAME = 'nextgens1'
GITHUB_URL = 'https://github.com/nextgens'
EMAIL='florent-blog@daigniere.com'
SOCIAL = (('Twitter', 'https://twitter.com/nextgens1'),
          ('Linkedin', 'https://linkedin.com/in/nextgens'),
	  ('Github', 'https://github.com/nextgens/'),)
# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('You can modify those links in your config file', '#'),)

LINKS = SOCIAL

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME='theme/pelican-svbtle'
STATIC_PATHS = ['CNAME', 'florent.daigniere.pubkey.txt',]
PLUGIN_PATH = 'pelican-plugins'
PLUGINS=['sitemap', ]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DISQUS_SITENAME = u'http://florent.daigniere.com/'
DISQUS_SECRET_KEY = u'aEOm9ZnCmrw1yl9E14FwYXO2UTAQ1cOiy8GI6CMd3YDl6F3VywolXLJQattttmNo'
DISQUS_PUBLIC_KEY = u'VsjlZZqF4CmwAB39p0evBjF5KDyNb0o5Tyfb7euKF3SuAY2y1hMx2ubB0VFBG3rZ'
