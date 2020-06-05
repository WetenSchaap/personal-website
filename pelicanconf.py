#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Piet Swinkels'
SITENAME = 'Piet Swinkels'
SITETITLE = 'Piet Swinkels'
SITESUBTITLE = 'Tinkering with science and computers, and preferably both'
SITEDESCRIPTION = "Piet's Personal Website"
#SITEURL = "https://www.swnkls.nl"
SITELOGO = "/images/piet_512px.png"
FAVICON = "/images/favicon.ico"
LINKS_IN_NEW_TAB = 'external'
PATH = 'content'
DEFAULT_PAGINATION = False

STATIC_PATHS = ['images']

#copyright
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

# Ignore cache for development
LOAD_CONTENT_CACHE = True

# What to show on the sidebar and top:
# main menu  (I don't really like this to be honest)
MAIN_MENU = False
MENUITEMS = (("About me", '/about-me.html'),
             ("Research", '/research.html'),
             #etc,etc
            )
DISPLAY_PAGES_ON_MENU = False
#DISPLAY_CATEGORIES_ON_MENU = False

#links
LINKS = (('Home','/index.html'),
         ('About me','/pages/about-me.html'),
         ('Research','/pages/research.html'),
         ('Publications','/pages/publications.html'),
         ('Resume','/pages/resume.html'),
         ('Contact me','/pages/contact-me.html'),
        )

#'social'
# the first entry is the symbol (find @ https://icons8.com/line-awesome), the second the link.
# To make this work, we need to hack the default Flex theme a little bit.
SOCIAL = (("lab la-linkedin", "https://www.linkedin.com/in/pjm-swinkels/"),
          ("lab la-orcid", "https://orcid.org/0000-0002-6118-9746"),
          ("las la-server", "https://nas.swnkls.nl"),
          ("lab la-git-square", "https://git.swnkls.nl"),
          ("las la-cogs", "https://nginx.swnkls.nl"),
          ("las la-tv", "https://jellyfin.swnkls.nl"),
          ("las la-cloud-download-alt", "https://torrent.swnkls.nl"),
#          ("lab la-wikipedia-w", "https://wiki.swnkls.nl"), # took this offline, may change in future.
          ("las la-bookmark", "https://shiori.swnkls.nl"),
         )

# Apply a theme:
# Okay, this folder should be included in the repo, because I actually changed the Flex theme a little bit to make line awesome symbols work!
THEME = "../pelican-themes/Flex"
