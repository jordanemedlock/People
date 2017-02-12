
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
common = map(lambda x: 'common/'+x, ['jquery.min.js','processing.min.js','underscore.min.js', 'patterns.js'])
marbles_scripts = common + map(lambda x: 'marbles/'+x, ['models.js','views.js','home.js'])
mind_scripts = common + map(lambda x: 'mind/'+x, ['home.js'])


@app.route('/marbles')
def hello_world():
    global marbles_scripts
    return render_template('home.html', scripts=marbles_scripts)

@app.route('/marbles/test')
def test():
    global marbles_scripts
    src = marbles_scripts[:-1] + ['/marbles/test.js']
    return render_template('home.html', scripts=src)

@app.route('/mind')
def mind():
    global mind_scripts
    return render_template('mind/home.html', scripts=mind_scripts)
