from parser import make, rand_dict

from flask import Flask, render_template
app = Flask(__name__)

q, a = rand_dict(make('wordlist'))

@app.route('/')
def template():
	return render_template('index.html', q = q, a = False)

@app.route('/a')
def answer():
	return render_template('index.html', q = q, a = a)

if __name__ == '__main__':
    app.run(debug=True)
