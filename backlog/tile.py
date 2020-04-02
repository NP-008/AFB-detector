import py_wsi
import py_wsi.imagepy_toolkit as tk
import os

img_lst = os.listdir("/home/napasiri/python/AFB/include/image/raw1/")
file_dir = "/home/napasiri/python/AFB/include/image/raw1/"
db_location = "/home/napasiri/python/AFB/include/image/"
xml_dir = file_dir
patch_size = 64
level = 10
db_name = "tile"
overlap = 0
label_map = {}

turtle = py_wsi.Turtle(file_dir, db_location, db_name, xml_dir=xml_dir, label_map=label_map)
level_count, level_tiles, level_dims = turtle.retrieve_tile_dimensions(img_lst[0], patch_size = 64)
print("level count: " + str(level_count))
print("levle_tiles: " + str(level_tiles))
print("level_dimensions: " + str(level_dims))

turtle.sample_and_store_patches(patch_size=256, level=16, overlap=0, load_xml=False, limit_bounds=True)
