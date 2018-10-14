from parser import make

from flask import Flask, render_template
app = Flask(__name__)

questions, answers = make('wordlist')

@app.route('/')
def template():
	return render_template('index.html', data=questions)

@app.route('/a')
def answer():
	return render_template('index.html', data=answers)

if __name__ == '__main__':
    app.run(debug=True)
