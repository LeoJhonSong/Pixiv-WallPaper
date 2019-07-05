# Pixiv-WallPaper

Automatically set custom random Pivix Pictures as Wallpaper based on the API
provided by
[Pixiv Illustration Collection](https://github.com/OysterQAQ/Pixiv-Illustration-Collection),
to be specific, the URL
https://api.pixivic.com/illust?w_h_ratio=16-9&minWidth=1080&range=0.0001&isR18=false
in the script. Method of requiring particular type of picture can be learned in [Pixiv Illustration Collection](https://github.com/OysterQAQ/Pixiv-Illustration-Collection).

There are several parameters you can configure, like 📁where to put the cache
picture, ⏲the time period to update the wallpaper. The default configuration is
as followed 👇

```python
############################# Basic Configuration ##############################
# path to store the Picture cache
path = os.path.join(os.path.expanduser("~"), "Pictures/PixivWallPaperPicCache")
# time period to change the Picture (minutes)
period = 1
################################################################################
```

Take my Windows environment as an example, my home directory is
**C:/Users/LeoJh**, so my cache folder will be
**C:/Users/LeoJh/Pictures/PixivWallPaperPicCache**. The wallpaper will be
updated every one minute.

The script can start running invisibly by execute the batch file `Startup.bat`.
