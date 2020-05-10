#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Piet Swinkels'
SITENAME = 'Piet Swinkels'
SITETITLE = 'Piet Swinkels'
SITESUBTITLE = 'My personal website'
SITEDESCRIPTION = "Piet's Personal Website"
#SITEURL = "https://www.swnkls.nl"
SITELOGO = "images/piet.png"
FAVICON = 'images/favicon.ico'
LINKS_IN_NEW_TAB = 'external' 
PATH = 'content'
DEFAULT_PAGINATION = False

#copyright
#CC_LICENSE = {
#    "name": "Creative Commons Attribution-ShareAlike",
#    "version": "4.0",
#    "slug": "by-sa"
#}
COPYRIGHT_NAME = "Piet Swinkels"
COPYRIGHT_YEAR = "2020"


# colorscheme
THEME_COLOR = 'dark'
#THEME_COLOR_ENABLE_USER_OVERRIDE = True

# localization
TIMEZONE = 'Europe/Amsterdam'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Ignore cache for dev
LOAD_CONTENT_CACHE = False

# What to show on the sidebar:
DISPLAY_PAGES_ON_MENU = False
#DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (("About me", '{filename}/content/pages/about-me.md'),
             ("Research", '{filename}/content/pages/research.md'),
            )

LINKS = (('test','https:\\duck.go'),
         )

SOCIAL = (("lab la-linkedin", "https://www.linkedin.com/in/pjm-swinkels/"),
          ("lab la-orcid", "https://orcid.org/0000-0002-6118-9746"),
          ("las la-server", "https://nas.swnkls.nl"),
          ("lab la-git-square", "https://git.swnkls.nl"),
          ("las la-cogs", "https://nginx.swnkls.nl"),
          ("las la-tv", "https://jellyfin.swnkls.nl"),
          ("las la-cloud-download-alt", "https://deluge.swnkls.nl"),
          ("lab la-wikipedia-w", "https://wiki.swnkls.nl"),
          ("las la-bookmark", "https://shaarli.swnkls.nl"),
         )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Apply a theme:
THEME = "../pelican-themes/Flex"
