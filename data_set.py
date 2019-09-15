from lyrics import lyrics

class data_set:

	def __init__(self):
		self.data = self.load_songs_raw()

	def load_songs_raw(self):
		with open('ALL_SONGS_NAMES.txt', 'r', encoding="utf-8") as f:
			data = f.readlines()
		return data

	def splitParams(self, raw):
		return ('https://lyrics.fandom.com/' + raw[12:raw.find('" title')],raw[raw.find('">')+2:raw.find('</a>')])

	def load_objects(self):
		all_songs_objects = []

		for song_tup in self.data:
			formatted = self.splitParams(song_tup)
			song = lyrics(formatted[1], formatted[0])
			if(not song.content == 'None'):
				song.clean(True)
				all_songs_objects.append(song)

		self.obj_list = all_songs_objects
		self.validate()

	def __str__(self):
		str_list = ''
		for item in self.obj_list:
			str_list += str(item) + '\n\n\n'
		return str_list

	def validate(self):
		for item in self.obj_list:
			if(item.content == 'None'):
				obj_list.remove(item)
