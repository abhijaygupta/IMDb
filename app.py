from flask import Flask, request, render_template
import requests
import urllib2
from bs4 import BeautifulSoup


app = Flask(__name__)

# movie Class
class Movie(object):
    title = ""
    link = ""
    year = ""
    info = ""
    pic = ""

    # constructor
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def addEverythingElse(self, year, info, pic):
		self.year = year
		self.info = info
		self.pic = pic

def createMovie(title, link):
    movie = Movie(title, link)
    return movie

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def results():
	actors = request.form.getlist('actors[]')
	first = True
	good_movies = []

	for actor in actors:
		print 'starting for actor ' + actor
		if first:
			good_movies = findMoviesForActor(actor) #no intersection cause good_movies in empty at first
			first = False
		else:
			new_movies = findMoviesForActor(actor)
			
			#intersection
			titlesInOriginal = set(x.title for x in good_movies)  # All movie titles in good_movies
			intersection = [y for y in new_movies if y.title in titlesInOriginal] #intersection only if new movie titles are in good_movies

			good_movies = intersection

	#test
	# for e in good_movies:
	# 	print e.title
	# 	print e.link
	# 	print ''

	for movie in good_movies:
		findEverythingAboutMovie(movie)

	return render_template('results.html', good_movies = good_movies)

def findMoviesForActor(name):
	name = name.lower()

	imdbWebsite = 'imdb+'
	url = 'http://google.com/search?sourceid=navclient&btnI=1&q=' #imdbWebsite+%s
	url = url+imdbWebsite+'\"'+name+'\"'
	print url

	var = requests.get(url)
	print var.url

	html = urllib2.urlopen(var.url).read()
	soup = BeautifulSoup(html, "html.parser")

	content = soup.find("div", {"class": "filmo-category-section"})

	paras = content.findAll('b')

	moviesForThisActor = []
	for para in paras:
		title = para.getText()
		tempLink = para.find("a")["href"]
		#now extract actual link
		positionOfQuestionMark = tempLink.index('?')
		link = 'http://www.imdb.com' + tempLink[:positionOfQuestionMark] #subtring till question mark

		#now create movie object and append
		moviesForThisActor.append(createMovie(title, link))

	return moviesForThisActor

def findEverythingAboutMovie(movie):
	link = movie.link.lower()

	var = requests.get(link)
	print var.url

	html = urllib2.urlopen(var.url).read()
	soup = BeautifulSoup(html, "html.parser")

	yearHTML = soup.find("span", id="titleYear")
	year = yearHTML.getText()

	infoHTML = soup.find("div", {"class": "summary_text"})
	info = infoHTML.getText()

	picHTML = soup.find("div", {"class": "poster"})
	pic = picHTML.find("img")["src"]

	movie.addEverythingElse(year, info, pic)
	
	#test
	# print 'now priting movie stuff'
	# print movie.year
	# print movie.info
	# print movie.pic

	return movie

if __name__ == '__main__':
    app.run(debug=True)






