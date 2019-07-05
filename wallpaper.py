import os
import platform
import time
import ctypes
from urllib import request

# path to store the Picture cache
path = os.path.join(os.path.expanduser("~"), "Pictures/PixivWallPaperPicCache")
# time period to change the Picture (minutes)
period = 1

system = platform.system()
if not os.path.exists(path):
    os.mkdir(path)
picPath = os.path.join(path, "1.jpg")
# anti-anti-crawler: User-Agent
request_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}
url = "https://api.pixivic.com/illust?w_h_ratio=16-9&minWidth=1080&range=0.0001"

while True:
    if os.path.exists(picPath):
        os.remove(picPath)
    req = request.Request(url, headers=request_headers)
    print('getting URL of the Picture')
    try:
        realURL = request.urlopen(req).geturl()
    except:
        print('Error happened, trying again')
        continue
    print('Downloading')
    request.urlretrieve(realURL, picPath)
    print('Setting as wallpaper')
    if system == 'Windows':
        ctypes.windll.user32.SystemParametersInfoW(20, 0, picPath, 0)  # set pic as wallpaper
    if system == 'Linux':
        os.system('gsettings set org.gnome.desktop.background picture-uri "file:///%s"' % (picPath))
    print('zzzzz')
    time.sleep(period*60)  # time period to change the Pic









