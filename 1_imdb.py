import requests
import urllib2
from bs4 import BeautifulSoup

name1 = raw_input('Enter the first actor/actress name: ')
name2 = raw_input('Enter the second actor/actress name: ')

name1 = name2.lower()
nam2 = name2.lower()

#artist = '\"' + artist + ' '
#song = song + '\"'

imdbWebsite = 'imdb+'
url = 'http://google.com/search?sourceid=navclient&btnI=1&q=' #imdbWebsite+%s
url = url+imdbWebsite+'\"'+name1+'\"'
print url
