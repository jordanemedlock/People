
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, jsonify, make_response
from functools import wraps, update_wrapper
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lib.person import Person
from lib.util import json_dumps

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'
app.debug = True
app.jinja_env.globals.update(type=type)
app.jinja_env.filters["json"] = json_dumps


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r


@app.route('/')
@app.route('/mind/list')
def mind_list():
    global common
    return render_template('list.html', people=Person.list())


@app.route('/mind/<unique_id>/view')
def mind_view(unique_id):
    person = Person.load(unique_id)
    return render_template('view.html', person=person)

@app.route('/mind/<unique_id>/<action>', methods=['POST'])
def mind_action(unique_id, action):
    person = Person.load(unique_id)
    if action in person:
        res = person[action](request.form)
        return jsonify({'response':res})
    else:
        return jsonify({'response':'Failed to execute action: "' + action + '"'})










