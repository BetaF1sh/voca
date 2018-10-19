from parser import exel2dict, mix_dict

from flask import Flask, render_template
app = Flask(__name__)

q, a = mix_dict(exel2dict('wordlist'))

@app.route('/')
def template():
	return render_template('index.html', q = q)

@app.route('/a')
def answer():
	return render_template('index.html', q = q, a = a)

if __name__ == '__main__':
    app.run(debug=True)
