from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
	return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)