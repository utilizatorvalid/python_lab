# 5. Sa se scrie un script, care primeste de la linia de comanda (ca argument)
# un URL, si descarca in directorul curent toate imaginile (img src).
from urllib import request
import urllib
import sys
import os

from pyquery import PyQuery as pq

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("give me please and some valid url")
        exit(-1)
    url = args[1]
    response = urllib.request.urlopen(url).read().decode('utf-8', errors='ignore')
    d = pq(response)
    # load_button = d("._oidfu")
    # print(load_button)

    images_tags = d('img')
    image_sources = []
    for image in images_tags:
        img = pq(image)
        # print(img.attr('src'))
        image_sources.append(img.attr('src'))
    image_sources = list(set(image_sources))

    # print(image_sources)
    i = 0
    for src in image_sources:
        i +=1
        try:
            photo_content = urllib.request.urlopen(src).read()
            with open('ex5_photos/f{index}.png'.format(index=i),'wb') as f:
                f.write(photo_content)
            print('photo ',i, 'ok')
        except:
            print('error')
