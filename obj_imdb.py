import requests
import urllib2
from bs4 import BeautifulSoup

name1 = raw_input('Enter the first actor/actress name: ')
name2 = raw_input('Enter the second actor/actress name: ')

#name1 = "Robert Downey Junior"
#name2 = "Chris Evans" 
name1 = name1.lower()
name2 = name2.lower()

#artist = '\"' + artist + ' '
#song = song + '\"'

imdbWebsite = 'imdb+'
url = 'http://google.com/search?sourceid=navclient&btnI=1&q=' #imdbWebsite+%s
url = url+imdbWebsite+'\"'+name1+'\"'
print url

url2 = 'http://google.com/search?sourceid=navclient&btnI=1&q=' #imdbWebsite+%s
url2 = url2+imdbWebsite+'\"'+name2+'\"'
print url2


var = requests.get(url)
print var.url

html = urllib2.urlopen(var.url).read()
soup = BeautifulSoup(html, "html.parser")

content = soup.find("div", {"class": "filmo-category-section"})

#print content
paras = content.findAll('b')

#print paras

list1 = []
for para in paras:
	#print '\n'
	list1.append(para.getText())
	#print para.getText()


var2 = requests.get(url2)
print var2.url

html2 = urllib2.urlopen(var2.url).read()
soup2 = BeautifulSoup(html2, "html.parser")

content2 = soup2.find("div", {"class": "filmo-category-section"})

#print content2
paras2 = content2.findAll('b')

#print paras2

list2 = []
for para2 in paras2:
	#print '\n'
	list2.append(para2.getText())
	#print para.getText()
print '\n'

print list1
print(' ')
print list2
print(' ' )
print set(list1).intersection(list2)

#print set(list1) & set(list2)












