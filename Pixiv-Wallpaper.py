#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import platform
import time
import shutil
import ctypes
from urllib import request

############################# Basic Configuration ##############################
# path to store the Picture cache
path = os.path.join(os.path.expanduser("~"), "Pictures/Pixiv-WallPaper-Cache")
# time period to change the Picture (minutes)
period = 10
################################################################################

# detect if your platform is Windows or Linux
system = platform.system()
# anti-anti-crawler: User-Agent
request_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}
url = "https://api.pixivic.com/illust?w_h_ratio=16-9&minWidth=1080&range=0.0001&isR18=false&getDetail=true"

while True:
    req = request.Request(url, headers=request_headers)
    try:
        realURL = request.urlopen(req).geturl()
    except:
        print('Error happened, trying again to get URL of the picture')
        continue
    print('Got URL of the picture')
    picName = realURL[realURL.find('?id')+4:realURL.find('&title')]
    picPath = os.path.join(path, (picName + ".jpg"))
    # detect if the cache folder exist, if not, make one
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        # detect if there is cache pictures, if so, delete them
        shutil.rmtree(path)
        os.mkdir(path)
    request.urlretrieve(realURL, picPath)
    print('Picture downloaded')
    if system == 'Windows':
        # set pic as wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, picPath, 0)
    if system == 'Linux':
        # set pic as wallpaper
        # the first command is to make sure the script is able to change gsettings
        os.system('export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/ && gsettings set org.gnome.desktop.background picture-uri "file://%s"' % (picPath))
    print('Wallpaper updated')
    print('waiting for %d more minutes' % (period))
    time.sleep(period*60)  # time period to change the Pic

