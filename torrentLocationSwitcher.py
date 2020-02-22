#   step 4: go to /home/yovvel/testfolder/downloads/
#   step 5: move each *.torrent to /home/yovvel/testfolder/torrent/

import os

#   step 1: go to /home/yovvel/testfolder/torrent/
torrent_dir = "/home/yovvel/testfolder/torrent/"
torrent_dir_file = os.listdir(torrent_dir)

#   step 2: for each *.added file:
for item in torrent_dir_file:
    if item.endswith(".added"):
        #   step 3: remove file
        os.remove(os.path.join(torrent_dir, item))
