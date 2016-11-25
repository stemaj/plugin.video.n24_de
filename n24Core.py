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

        urlMain = "http://m.n24.de/n24/Nachrichten/Wetter";
        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain, True)

        self.error = stUrl.error;
        if len(self.error) > 0:
            return;

        match = re.compile('source src=\"(.+?)\" type', re.DOTALL).findall(dataMain)[0]
        return match

#TEST
#nC = N24Core()
#data = nC.getWeatherData()
#x = 0



        


