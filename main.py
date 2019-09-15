from lyrics import lyrics
from data_set import data_set

ds = data_set()
ds.load_objects()
for item in ds.obj_list:
	print(item.name, item.album)
