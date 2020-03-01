#! /usr/bin/python

import os
import shutil

#   step 1: go to /home/yovvel/testfolder/torrent/
torrent_dir = "smb://192.168.0.11/rpi-s-01-share/torrent/watch-dir/"
torrent_dir_file = os.listdir(torrent_dir)

downloads_dir ="/home/yovvel/Downloads/"
downloads_dir_file= os.listdir(downloads_dir)

added_files = 0
torrent_files = 0

#   step 2: for each *.added file:
for item in torrent_dir_file:
            #   step 3: remove file
    if item.endswith(".added"):
        added_files = added_files +  1
        os.remove(os.path.join(torrent_dir, item))

#   step 4: go to /home/yovvel/testfolder/downloads/
for item in downloads_dir_file:
    #   step 5: move each *.torrent to /home/yovvel/testfolder/torrent/
    if item.endswith(".torrent"):
		torrent_files = torrent_files +  1
        shutil.move(downloads_dir + item, torrent_dir)


#give some feedback to the user about how many files are removed and moved
if added_files > 1:
    print(str(added_files) + " *.added files removed")
elif added_files == 1:
    print("Only 1  *.added found and removed")

elif added_files 0= 0:
    print("no *.added files removed")

if torrent_files > 1:
    print(str(torrent_files) + " new torrent download files have been added")
elif torrent_files == 1:
    print("1 new torrent file added")

elif torrent_files == 0:
    print("no Torrent files found")
