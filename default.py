#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import socket
import re
import sys
import os
import xbmcplugin
import xbmcaddon
import xbmcgui
from n24Core import N24Core

socket.setdefaulttimeout(30)
pluginhandle = int(sys.argv[1])
addonId = 'plugin.video.wettervorhersage'
addon = xbmcaddon.Addon(id=addonId)
addonDir = xbmc.translatePath(addon.getAddonInfo('path'))
fanart = os.path.join(addonDir ,'fanart.jpg')
icon = os.path.join(addonDir ,'icon.png')

def index():

    #addLink("ZDF - So wird das Wetter", "1", 'playWeather', "")
    addLink("wetter.com - Aktuell", "2", 'playWeather', "")
    addLink("wetter.com - Vorschau", "3", 'playWeather', "")
    addLink("wetter.com - Regionalwetter Sachsen", "6", 'playWeather', "")
    addLink("n-tv wetter", "4", 'playWeather', "")
    addLink("wetter.info", "5", 'playWeather', "")
    addLink("Wetter für 3 - mdr.de", "7", 'playWeather', "")
    xbmcplugin.endOfDirectory(pluginhandle)

def playWeather(nr):
    nC = N24Core()
    if nr == "2":
        data = nC.getNtvWetterComAktuellVideo()
    elif nr == "3":
        data = nC.getNtvWetterComVorschauVideo()
    elif nr == "6":
        data = nC.getWetterComSachsenVideo()
    elif nr == "4":
        data = nC.getNtvWetterVideo()
    elif nr == "5":
        data = nC.getWetterInfoVideo()
    elif nr == "7":
        data = nC.getMdrVideo()

    if (len(nC.error) > 0):
        notification(nC.error)
        return

    listitem = xbmcgui.ListItem(path=data, thumbnailImage=icon, iconImage=fanart)
    xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)

def addLink(name, url, mode, iconimage):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+urllib.quote_plus(mode)+"&name="+urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name)
    liz.setProperty("fanart_image", fanart)
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)
    return ok

def parameters_string_to_dict(parameters):
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

params = parameters_string_to_dict(sys.argv[2])
mode = urllib.unquote_plus(params.get('mode', ''))
url = urllib.unquote_plus(params.get('url', ''))
name = urllib.unquote_plus(params.get('name', ''))

if mode == 'playWeather':
    playWeather(url)
else:
    index()
