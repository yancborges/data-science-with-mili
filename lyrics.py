import imp
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import urllib.request
import re
import decimal

class lyrics:

	def __init__(self, name, url):
		self.name = name
		self.url = url
		if(self.validName()):
			try:
				data = self.open()
			except:
				self.save()
				data = self.open()
			self.album = data[0][1:-2]
			self.content = data[1:]
		else:
			self.content = "None"
			self.album = 'None'

	def validName(self):
		name_splitted = word_tokenize(self.name)
		for word in name_splitted:
			if(not wordnet.synsets(word)):
				return False
		return True

	def open(self):
		with open('C://Users//Yan//Documents//GitHub//data-science-with-mili//lyrics//' + self.name.replace(' ','_') + '.txt', 'r', encoding="utf-8") as f:
			data = f.readlines()
			return data

	def save(self):
		resp = urllib.request.urlopen(self.url).read().decode('utf8')
		with open( 'C://Users//Yan//Documents//GitHub//data-science-with-mili//lyrics//' + self.name.replace(' ', '_') + '.txt', 'w', encoding="utf-8") as f:
			text = re.findall(r'<div class=\'lyricbox\'>.+<div',resp)[0]
			#f.write(self.decode(text))
			f.write(text.decode('utf8'))

	def __str__(self):
		return ('%s - %s\nLyrics: %s' %(self.name, self.album, self.format_content()))

	def decode(self, text):
		blocks = text.replace('<br />','\n').split(';')
		decoded = ''
		for item in blocks:
			decoded += str(item[2:])
		return decoded


	def clean(self, inplace):
		data = self.content
		clean_lyrics = []
		ignore_count = 0
		stop_words = stopwords.words('english')
		for phrase in data[1:]:
			phrase_splitted = word_tokenize(phrase.replace('\n', ''))
			clean_phrase = []
			for word in phrase_splitted:
				if wordnet.synsets(word) and not word in stop_words:
					clean_phrase.append(word)
				else:
					ignore_count += 1
					print('%s words ignored in %s' %(ignore_count, self.name))
			clean_lyrics.append(clean_phrase)
		if(inplace == False):
			return clean_lyrics
		else:
			self.content = clean_lyrics

	def format_content(self):
		lyrics = ""
		for phrase in self.content:
			for word in phrase:
				lyrics += word + " "
		return lyrics
