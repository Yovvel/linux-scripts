#   step 1: go to /home/yovvel/testfolder/torrent/
#   step 2: for each *.added file:
#   step 3: remove file

#   step 4: go to /home/yovvel/testfolder/downloads/
#   step 5: move each *.torrent to /home/yovvel/testfolder/torrent/





import os

torrent_dir = "/home/yovvel/testfolder/torrent/"
torrent_dir_file = os.listdir(torrent_dir)

for item in torrent_dir_file:
    if item.endswith(".added"):
        os.remove(os.path.join(torrent_dir, item))
