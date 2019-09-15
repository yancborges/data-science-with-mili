import urllib.request
import re

URL = 'https://lyrics.fandom.com/wiki/Mili'

resp = urllib.request.urlopen(URL).read().decode("utf-8")
tags = re.findall(r'<b><a href=\S+ title=".+</a></b>', resp)

with open('ALL_SONGS_NAMES.txt', 'w', encoding='utf-8') as f:
	for item in tags:
		f.write(item + "\n")
	