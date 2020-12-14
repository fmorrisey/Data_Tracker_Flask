from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests as rs
import json as js
from types import SimpleNamespace

bp = Blueprint('sample', __name__)

""""""

json_data = dict


def api_request():  # Handle errors gracefully
    response = rs.get("https://api.dccresource.com/api/games")
    game_data = js.loads(response.content, object_hook=lambda d: SimpleNamespace(**d)) \
        if response and response.status_code == 200 else None
    return json_data

    return game_data


@bp.route('/', methods=['GET'])
def search():
    return render_template('sample/search.html')


@bp.route('/search/results', methods=['GET', 'POST'])
def search_requests():
    search_term = request.form["input"]

    game_data = api_request()

    results = search()

    return render_template('results.html', res=results)


""""""""


@bp.route('/test')
def test():
    return "All good!"


@bp.route('/sample')  # URL Route
def index():  # Index.html
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('sample/index.html', message=message, word=phrase)


@bp.route('/postform', methods=('GET', 'POST'))
def other_example():
    if request.method == 'POST':
        page_title = request.form['title']
        error = None

        if not page_title:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        elif request.form['title'] == "go home":  # Redirect to another page
            return redirect(url_for('sample.index'))
        else:
            return render_template('sample/postform.html', page_title=page_title)

    else:
        return render_template('sample/postform.html', page_title="PostForm from Module Function")
