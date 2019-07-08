import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from resources.lib import main
from resources.lib import read

class Test_1(unittest.TestCase):

  def test_1(self):
    data = read.load_file('000')
    arr = main.listOfNewest(data)
    self.assertEqual(10, len(arr))
    self.assertEqual('Wetter heute: Tiefpunkt zu Wochenbeginn', arr[2].film)
    self.assertEqual('https://www.wetter.com/videos/deutschlandwetter/wetter-heute/56cba782217091ab20000030', arr[2].link)

  def test_2(self):
    data = read.load_file('001')
    link = main.getVideoLink(data)
    self.assertEqual('https://cv2.wettercomassets.com/video-updates/2019/07/08/7-tage-trend-was-fuer-eine-turbulente-mist-woche_57cd6c56cebfc040448b4567/5d2323cd7bb3f/720p.mp4', link)

