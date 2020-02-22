#! /usr/bin/python

import os
import shutil

#   step 1: go to /home/yovvel/testfolder/torrent/
torrent_dir = "/home/yovvel/testfolder/torrent/"
torrent_dir_file = os.listdir(torrent_dir)

downloads_dir ="/home/yovvel/testfolder/downloads/"
downloads_dir_file= os.listdir(downloads_dir)

added_files = 0

#   step 2: for each *.added file:
for item in torrent_dir_file:
            #   step 3: remove file
    if item.endswith(".added"):
        added_files = added_files +  1
        os.remove(os.path.join(torrent_dir, item))
if added_files > 1:
    print(str(added_files) + " *.added files removed")
elif added_files == 1:
    print("Only 1  *.added found and removed")

else:
    print("no *.added files removed")


#   step 4: go to /home/yovvel/testfolder/downloads/
for item in downloads_dir_file:
    #   step 5: move each *.torrent to /home/yovvel/testfolder/torrent/
    if item.endswith(".torrent"):
        shutil.move(downloads_dir + item, torrent_dir)
