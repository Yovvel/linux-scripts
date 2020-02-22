#! /usr/bin/python

import os
import shutil

#   step 1: go to /home/yovvel/testfolder/torrent/
torrent_dir = "/home/yovvel/testfolder/torrent/"
torrent_dir_file = os.listdir(torrent_dir)

downloads_dir ="/home/yovvel/testfolder/downloads/"
downloads_dir_file= os.listdir(downloads_dir)

#   step 2: for each *.added file:
for item in torrent_dir_file:
            #   step 3: remove file
    if item.endswith(".added"):
        os.remove(os.path.join(torrent_dir, item))

#   step 4: go to /home/yovvel/testfolder/downloads/
for item in downloads_dir_file:
    #   step 5: move each *.torrent to /home/yovvel/testfolder/torrent/
    if item.endswith(".torrent"):
        shutil.move(downloads_dir+item, torrent_dir)
