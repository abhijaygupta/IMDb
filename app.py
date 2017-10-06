from flask import Flask, request, render_template
import requests
import urllib2
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def results():
	# actor1 = request.form['actor1']
	# actor2 = request.form['actor2']
	actor1 = "brad pitt"
	actor2 = "angelina jolie"
	bad_movies = list(findMovies(actor1, actor2))
	good_movies = []
	for movie in bad_movies:
		good_movies.append(str(movie))
	print good_movies
	fullList = []
	obj = {'title': 'Mr. & Mrs. Smith', 'year': '2005', 'link': 'http://www.imdb.com/title/tt0356910/', 'info': 'A bored married couple is surprised to learn that they are both assassins hired by competing agencies to kill each other.', 'pic': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxMzcxNzQzOF5BMl5BanBnXkFtZTcwMzQxNjUyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg'} 
	fullList.append(obj)
	fullList.append(obj)
	print fullList
	return render_template('results.html', allMovies = fullList)

def findMovies(name1, name2):
	name1 = name1.lower()
	name2 = name2.lower()

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

	paras = content.findAll('b')

	list1 = []
	for para in paras:
		list1.append(para.getText())

	var2 = requests.get(url2)
	print var2.url

	html2 = urllib2.urlopen(var2.url).read()
	soup2 = BeautifulSoup(html2, "html.parser")

	content2 = soup2.find("div", {"class": "filmo-category-section"})

	paras2 = content2.findAll('b')

	list2 = []
	for para2 in paras2:
		list2.append(para2.getText())

	return set(list1).intersection(list2)

if __name__ == '__main__':
    app.run(debug=True)






