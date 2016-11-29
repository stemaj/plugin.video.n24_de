#!/usr/bin/python
# -*- coding: utf-8 -*-

from stemajUrl import *

class N24Core(object):

    def __init__(self, *args, **kwargs):
        return super(N24Core, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(N24Core, self).__str__()

    error = "";

    def getWeatherData(self):

        #urlMain = "http://m.n24.de/n24/Nachrichten/Wetter";
        #stUrl = StemajUrl()
        #dataMain = stUrl.getUrl(urlMain, True)

        #self.error = stUrl.error;
        #if len(self.error) > 0:
        #    return;

        #match = re.compile('source src=\"(.+?)\" type', re.DOTALL).findall(dataMain)[0]
        #return match
        return "http://dlc3.t-online.de/mflash/wetterstudio_prem.mp4"

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

        name = re.compile("name\": \"(.+?)\",", re.DOTALL).findall(dataMain)[0]
        match = re.compile("contentUrl\": \"(.+?)\"", re.DOTALL).findall(dataMain)[0]
        return (name,match)


#TEST
#nC = N24Core()
#data = nC.getWeatherComUrls()
#vid = ()
#for dat in data:
#    vid = nC.getWeatherComVid(dat)

#x = 0



        


