# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory


ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


@plugin.route('/')
def index():
    data = read.load_url("https://www.wetter.com/videos/deutschlandwetter/")
    arr = main.listOfNewest(data)
    for x in arr:
        data2 = read.load_url(x.link)
        link = main.getVideoLink(data2)
        listItem = ListItem(path=link , label=x.film)
        listItem.setProperty('IsPlayable', 'true')
        addDirectoryItem(plugin.handle, link, listItem)
    endOfDirectory(plugin.handle)

def run():
    plugin.run()
