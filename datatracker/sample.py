from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from elasticsearch import Elasticsearch
import requests as rp

bp = Blueprint('sample', __name__)
es = Elasticsearch('10.0.1.10', port=9200)
""""""

json_data = dict

def api_request():      #Handle errors gracefully
    response = rp.get("https://api.dccresource.com/api/games")
    json_data = response.json() if response and response.status_code == 200 else None
    return json_data
    #return jsonify({json_data})

@bp.route('/', methods=['GET'])
def search():

    return render_template('sample/search.html')

@bp.route('/search/results', methods=['GET', 'POST'])
def search_requests():
    search_term = request.form["input"]
    json_data = api_request()
    res = es.search(
    )


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
        elif request.form['title'] == "go home":                    # Redirect to another page
            return redirect(url_for('sample.index'))
        else:
            return render_template('sample/postform.html', page_title=page_title)

    else:
        return render_template('sample/postform.html', page_title="PostForm from Module Function")
