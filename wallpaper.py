import os
import platform
import time
import ctypes
from urllib import request

############################# Basic Configuration ##############################
# path to store the Picture cache
path = os.path.join(os.path.expanduser("~"), "Pictures/PixivWallPaperPicCache")
# time period to change the Picture (minutes)
period = 1
################################################################################

# detect if your platform is Windows or Linux
system = platform.system()
picPath = os.path.join(path, "1.jpg")
# anti-anti-crawler: User-Agent
request_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}
url = "https://api.pixivic.com/illust?w_h_ratio=16-9&minWidth=1080&range=0.0001&isR18=false"

while True:
    # detect if the cache folder exist, if not, make one
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        # detect if there is cache picture, if so, delete it
        if os.path.exists(picPath):
            os.remove(picPath)
    req = request.Request(url, headers=request_headers)
    try:
        realURL = request.urlopen(req).geturl()
    except:
        print('Error happened, trying again')
        continue
    print('Got URL of the Picture')
    request.urlretrieve(realURL, picPath)
    print('Picture downloaded')
    if system == 'Windows':
        # set pic as wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, picPath, 0)
    if system == 'Linux':
        # set pic as wallpaper
        os.system('gsettings set org.gnome.desktop.background picture-uri "file:///%s"' % (picPath))
    print('Wallpaper updated')
    print('waiting for %d more minutes' % (period))
    time.sleep(period*60)  # time period to change the Pic









