# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory, setResolvedUrl
import read
import main

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


@plugin.route('/')
def index():
    data = read.load_url("https://www.wetter.com/videos/")
    arr = main.listOfNewest(data)
    for x in arr:
        listItem = ListItem(label=x.film)
        repl = x.link.replace('/','_')
        listItem.setProperty('IsPlayable', 'true')
        addDirectoryItem(plugin.handle, plugin.url_for(play_video, repl), listItem)
    endOfDirectory(plugin.handle)

@plugin.route('/category/<video_id>')
def play_video(video_id):
    video_url = video_id.replace('_','/')
    data2 = read.load_url(video_url)
    link = main.getVideoLink(data2)
    play_item = ListItem(path=link)
    setResolvedUrl(plugin.handle, True, listitem=play_item)

def run():
    plugin.run()
