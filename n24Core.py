#!/usr/bin/python
# -*- coding: utf-8 -*-

from stemajUrl import *

class N24Core(object):

    def __init__(self, *args, **kwargs):
        return super(N24Core, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(N24Core, self).__str__()

    error = "";

    def getWeatherData(self, nr):

        if nr == "2":
            return "http://dlc3.t-online.de/mflash/wetterstudio_prem.mp4"
        
        return "https://zdfvodnone-vh.akamaihd.net/i/meta-files/zdf/smil/m3u8/300/16/10/161026_1900_wet/1/161026_1900_wet.smil/master.m3u8"


    def getWeatherComUrls(self):

        urlMain = "http://www.wetter.com/videos/deutschlandwetter/";
        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain, True)

        self.error = stUrl.error;
        if len(self.error) > 0:
            return;

        dataMain = dataMain.split("Videos gefunden.")[1];
        dataMain = dataMain.split("var domNode")[0];
        dataMain = dataMain.split("<div class=\"relative mb-\">");
        dataMain.pop(0)

        match = []
        for data in dataMain:
            match.append(re.compile('href=\"(.+?)\">', re.DOTALL).findall(data)[0])
        return match

    def getWeatherComVid(self, urlMain):

        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain, True)

        self.error = stUrl.error;
        if len(self.error) > 0:
            return;

        match = re.compile("itemprop=\"contentUrl\" content=\"(.+?)\">", re.DOTALL).findall(dataMain)[0]
        name = re.compile("itemprop=\"name\">(.+?)</h3>", re.DOTALL).findall(dataMain)[0]
        return (name,match)


##TEST
#nC = N24Core()
#data = nC.getWeatherComUrls()
#vid = ()
#for dat in data:
#    vid = nC.getWeatherComVid(dat)

#x = 0



        


