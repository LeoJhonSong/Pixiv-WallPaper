# Pixiv-WallPaper

Automatically set custom random Pivix Pictures as Wallpaper based on the API
provided by [Pixiv Illustration
Collection](https://github.com/OysterQAQ/Pixiv-Illustration-Collection), to be
specific, the URL
https://api.pixivic.com/illust?w_h_ratio=16-9&minWidth=1080&range=0.0001&isR18=false
in the script. Method of requiring particular type of picture can be learned in
[Pixiv Illustration
Collection](https://github.com/OysterQAQ/Pixiv-Illustration-Collection).

## Prerequirements

❗️a python3 which is added to PATH is needed.

python library `requests` is needed

run `import requests` in python to check if you have it. if you don't, run
`pip install requests` to get it.

## Installation

```shell
git clone git@github.com:LeoJhonSong/Pixiv-WallPaper.git

# give permission to execute to Pixiv-Wallpaper.py and Startup.sh
chmod a+x Pixiv-Wallpaper.py Startup.sh
```

## Configuration

There are several parameters you can configure, like 📁where to put the cache
picture, ⏲the time period to update the wallpaper. The default configuration is
as followed 👇

```python
############################# Basic Configuration ##############################
# path to store the Picture cache
path = os.path.join(os.path.expanduser("~"), "Pictures/Pixiv-WallPaper-Cache")
# time period to change the Picture (minutes)
period = 1
################################################################################
```

Take my Windows environment as an example, my home directory is
**C:/Users/LeoJh**, so my cache folder will be
**C:/Users/LeoJh/Pictures/Pixiv-WallPaper-Cache**. The wallpaper will be
updated every one minute.

## Windows

The script can start running invisibly by execute the batch file `Startup.bat`.
You can even set the script to startup automatically every time power up by
modifying the `Startup.vbs` and put it in
**C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup**

## Linux

Since I am using gnome, as a lazy bone, only gnome is supported.

The script can start running invisibly by execute the shell script `Startup.sh`.
