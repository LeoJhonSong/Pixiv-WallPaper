# run the script as a job
# the standard output is thrown away
# the standard error output is saved to error.log
nohup ./Pixiv-Wallpaper.py 1>/dev/null 2>error.log & echo "Start running"
