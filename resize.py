#coding=utf-8
#!/usr/bin/python

import os
import sys
import commands
from PIL import Image

#lst = commands.getoutput('find /data/htdocs/images/goods/s5 -name "*_S.jpg"')
lst = commands.getoutput('find /data/htdocs/images/goods/1110 -name "*_S.jpg"')
fa = lst.split('\n')
for fs in fa:
  im = Image.open(fs)
  w,h = im.size
  if w != h:
    print('####NOT SQUARE: ' + fs, w, h)
    continue
  im0 = im.resize((306,306), Image.ANTIALIAS)
  #im.save(fs+'.jpg')
  im0.save(fs)
