import re

def increment(i):
  return i+1

class Film():
  def __init__(self, film, link):
        self.film = film
        self.link = link

def listOfNewest(bytes):
  split1 = bytes.decode('utf-8').split('Empfehlungen')[1]
  split2 = split1.split('Video-Channels')[0]
  splits3 = split2.split('anchor--section')
  splits4 = splits3[1:len(splits3)]

  regex = r"href=\"(.+)\".+data-p.+title=\"(.+)\"><d"
  
  filme = []
  for data in splits4:
      data = data.replace("\n","\\n")
      data = data.replace("\t","\\t")
      data = data.replace("\'","\\\'")
      matches = re.findall(regex, data, re.MULTILINE)
      if len (matches) > 0:
        film = Film(matches[0][1], matches[0][0])
        filme.append(film)
  return filme

def getVideoLink(bytes):
  split1 = bytes.decode('utf-8')
  regex = r"data-video-url-hd=\"(.+)\""
  matches = re.findall(regex, split1, re.MULTILINE)
  if len (matches) > 0:
    return matches[0]

