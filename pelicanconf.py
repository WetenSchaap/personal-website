#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Piet Swinkels'
SITENAME = 'Piet Swinkels'
SITETITLE = 'Piet Swinkels'
SITESUBTITLE = 'My personal website'
SITEDESCRIPTION = "Piet's Personal Website"
#SITEURL = "https://www.swnkls.nl"
FAVICON = 'images/favicon.ico'

# colorscheme
THEME_COLOR = 'dark'
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# What to show on the sidebar:

DISPLAY_PAGES_ON_MENU = False
#DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (("About me", '/about-me.html'),
            )

LINKS = (('NAS', 'https://nas.swnkls.nl'),
         ('Wiki', 'https://wiki.swnkls.nl'),
         ('Jellyfin', 'https://jellyfin.swnkls.nl'),
         ('Deluge', 'https://deluge.swnkls.nl'),
         ('Git', 'https://git.swnkls.nl'),
         ('Nginx', 'https://nginx.swnkls.nl'),
         ('Shaarli', 'https://shaarli.swnkls.nl'),
         )

SOCIAL = (("linkedin", "https://www.linkedin.com/in/pjm-swinkels/"),
          ("orcid", "https://orcid.org/0000-0002-6118-9746"),
          ("fa-server", "https://nas.swnkls.nl"),
          ("git", "https://git.swnkls.nl"),
          ("cogs", "https://nginx.swnkls.nl"),
          ("tv", "https://jellyfin.swnkls.nl"),
          ("cloud-download-alt", "https://deluge.swnkls.nl"),
          ("wikipedia-w", "https://wiki.swnkls.nl"),
          ("bookmark", "https://shaarli.swnkls.nl"),
         )

# Social widget
#SOCIAL = (('ORCID', 'https://orcid.org/0000-0002-6118-9746'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Apply a theme:
THEME = "../pelican-themes/Flex"
