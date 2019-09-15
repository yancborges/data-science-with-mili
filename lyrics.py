import imp
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class lyrics:

	def __init__(self, name, url):
		self.name = name
		self.url = url
		if(self.validName()):
			data = self.open()
			self.album = data[0][1:-2]
			self.content = data[1:]
		else:
			return False

	def validName(self):
		name_splitted = word_tokenize(self.name)
		for word in name_splitted:
			if(not wordnet.synsets(word)):
				return False
		return True

	def open(self):
		with open('C://Users//Yan//Documents//GitHub//data-science-with-mili//lyrics//' + self.name + '.txt', 'r', encoding="utf-8") as f:
			data = f.readlines()
			return data
			

	def __str__(self):
		return ('%s - %s\nLyrics: %s' %(self.name, self.album, self.format_content()))


	def clean(self, inplace):
		data = self.open()
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
					print('%s words ignored' %ignore_count)
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
