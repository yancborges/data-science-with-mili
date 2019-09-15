import urllib.request

urls = ['https://www.letras.mus.br/mili/','https://lyrics.fandom.com/wiki/Mili','https://www.musixmatch.com/artist/MILI','https://lyricstranslate.com/en/mili-lyrics.html']

errors = 0
for url in urls:
	try:
		resp = urllib.request.urlopen(url).read().decode("utf-8")
	except Exception as e:
		resp = str(e)
		errors += 1

	with open('C://Users//Yan//Documents//GitHub//data-science-with-mili//html_test//' + url.split('//')[1].split('/')[0] + '.html', 'w', encoding='utf-8') as f:
		f.write(resp)

print('%d sites checked, %d errors raised' %(len(urls), errors)) 

