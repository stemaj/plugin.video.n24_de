import re

def increment(i):
  return i+1

class Film():
  def __init__(self, film, link, plot):
        self.film = film
        self.link = link
        self.plot = plot

def listOfNewest(bytes):
  split1 = bytes.decode('utf-8').split('weitere Predigten')[1]
  split2 = split1.split('footer id')[0]
  splits3 = split2.split('<figure class=')
  splits4 = splits3[1:len(splits3)]

  regex = r"src=\"(.+)\".+ong>(.+)</strong>(.+)</figc"
  
  filme = []
  for data in splits4:
      matches = re.findall(regex, data, re.MULTILINE)
      if len (matches) > 0:
        film = Film(matches[0][2], matches[0][0], matches[0][1])
        filme.append(film)
  return filme