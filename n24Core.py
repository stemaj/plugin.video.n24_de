#!/usr/bin/python
# -*- coding: utf-8 -*-

from stemajUrl import *
#import requests
#import json

class N24Core(object):

    def __init__(self, *args, **kwargs):
        return super(N24Core, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(N24Core, self).__str__()

    error = "";


    def getNtvWetterVideo(self):

        urlMain = "http://www.n-tv.de/wetter/"
        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('<li class=\"teaser-media\">(.+?)\" title=', re.DOTALL).findall(dataMain)
        link = ""
        if len(match) > 0:
            link = splitStartingFrom(match[0], "href=\"")[0]
        else:
            error = "Parse Error"
            return

        dataMain2 = stUrl.getUrl(link)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return
       
        match = re.compile('videoM3u8: \"(.+?)\",', re.DOTALL).findall(dataMain2)
        if len(match) > 0:
            return match[0]

        error = "Parse Error"
        return


    def getNtvWetterComAktuellVideo(self):

        urlMain = "http://www.wetter.com/videos/"
        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain, True)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('meta itemprop=\"contentUrl\" content=\"(.+?)\">', re.DOTALL).findall(dataMain)
        if len(match) > 0:
            return match[0]

        error = "Parse Error"
        return

    def getNtvWetterComVorschauVideo(self):

        urlMain = "http://www.wetter.com/videos/"
        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain, True)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('href=\"/videos/wochenendwetter/(.+?)\"', re.DOTALL).findall(dataMain)
        if len(match) < 1:
            error = "Parse Error"
            return

        url2 = urlMain + "wochenendwetter/" + match[0]
        dataMain2 = stUrl.getUrl(url2, True)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('meta itemprop=\"contentUrl\" content=\"(.+?)\">', re.DOTALL).findall(dataMain2)
        if len(match) > 0:
            return match[0]

        error = "Parse Error"
        return

    def getWetterComSachsenVideo(self):

        urlMain = "http://www.wetter.com/videos/regionalwetter"
        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain, True)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('regionalwetter/sachsen(.+?)\" title=\"Sachsen', re.DOTALL).findall(dataMain)
        if len(match) < 2:
            error = "Parse Error"
            return

        url2 = urlMain + "/sachsen" + match[1]
        dataMain2 = stUrl.getUrl(url2, True)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('meta itemprop=\"contentUrl\" content=\"(.+?)\">', re.DOTALL).findall(dataMain2)
        if len(match) > 0:
            return match[0]

        error = "Parse Error"
        return


    def getMdrVideo(self):

        urlMain = "http://www.mdr.de/mediathek/fernsehen/a-z/wetterfr100_zc-ca8ec3f4_zs-73445a6d.html"
        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain, True)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('a href=\"/mediathek/fernsehen/a-z/sendung7(.+?).html', re.DOTALL).findall(dataMain)
        if len(match) < 1:
            error = "Parse Error"
            return

        url2 = "http://www.mdr.de/mediathek/fernsehen/a-z/sendung7" + match[0] + ".html";
        dataMain2 = stUrl.getUrl(url2, True)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('/video-(.+?).xml', re.DOTALL).findall(dataMain2)
        if len(match) < 1:
            error = "Parse Error"
            return

        url3 = "http://www.mdr.de/mediathek/fernsehen/a-z/video-" + match[0] + ".xml";
        dataMain3 = stUrl.getUrl(url3, True)
        if len(stUrl.error) > 0:
            error = stUrl.error
            return

        match = re.compile('<progressiveDownloadUrl>(.+?)</progressiveDownloadUrl>', re.DOTALL).findall(dataMain3)
        if len(match) > 0:
            return match[0]

        error = "Parse Error"
        return

    def getWetterInfoVideo(self):

        return "http://dlc3.t-online.de/mflash/wetterstudio_prem.mp4"


    #def getZdf(self):

        ##'https://zdfvodnone-vh.akamaihd.net/i/meta-files/zdf/smil/m3u8/300/16/10/161026_1900_wet/1/161026_1900_wet.smil/master.m3u8'

        #auth = '23a1db22b51b13162bd0b86b24e556c8c6b6272d reraeB'
        #results = requests.get("https://api.zdf.de/search/documents", params={'q': 'so wird das wetter', 'Api-Auth': auth[::-1]})

        #str = ""
        #for res in results:
        #    str += res

        ##urlMain = "https://api.zdf.de/search/documents?q=so wird das wetter"
        ##stUrl = StemajUrl()
        ##dataMain = stUrl.getUrl(urlMain)
        #j = json.loads(str)
        #k = j[u'http://zdf.de/rels/search/results']
        #l = k[1][u'http://zdf.de/rels/target']
        #m = l[u'mainVideoContent']
        #n = m[u'http://zdf.de/rels/target']
        #o = n[u'http://zdf.de/rels/streams/ptmd-template']
        #p = 'https://api.zdf.de' + o
        #p = p.replace('{playerId}','ngplayer_2_3')

        ##p = "https://api.zdf.de/content/documents/zdf/nachrichten/heute/so-wird-das-wetter-100.json?profile=teaser"

        #res3 = requests.get(p, params={'Api-Auth': auth[::-1]})
        #str2 = ""
        #for res in res3:
        #    str2 += res

        #s = json.loads(str2)

        ##res2 = requests.get("https://api.zdf.de/content/documents/so-wird-das-wetter-100.json", params={'q': 'so wird das wetter', 'Api-Auth': auth[::-1]})


#TEST
#nC = N24Core()
#nC.getMdrVideo()

