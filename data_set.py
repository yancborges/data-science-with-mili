from lyrics import lyrics

def load_songs():
	with open('ALL_SONGS_NAMES.txt', 'r', encoding="utf-8") as f:
		data = f.readlines()
	return data

def splitParams(raw):
	return ('https://lyrics.fandom.com/' + raw[12:raw.find('" title')],raw[raw.find('">')+2:raw.find('</a>')])

ALL_SONGS_NAMES = load_songs()
all_songs_objects = []

'''
for song_tup in ALL_SONGS:
	song = lyrics(song_tup)
	song.clean(True)
	all_songs_objects.appeend(song)
'''

for song in ALL_SONGS_NAMES:
	try:
		print(splitParams(song))
	except:
		pass
print(len(ALL_SONGS_NAMES))