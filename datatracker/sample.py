from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint, session
from datatracker.platformData import platformData as pfd
from datatracker.api import api
from datatracker.search import search as srch
import json


bp = Blueprint('sample', __name__)

results = []


@bp.route('/search', methods=['GET'])
def search():
    return render_template('sample/search.html')


@bp.route('/search/results', methods=['GET', 'POST'])
def search_requests():
    search_term = request.form["input"]
    game_Data = api.requests_NameSpace("https://api.dccresource.com/api/games")
    results, hits = srch.searchByName(game_Data, search_term)
    #userResults = json.dumps(results)
    #session['userResults'] = userResults
    return render_template('sample/results.html', res=results, hits=hits, num=1)


@bp.route('/search/details/<game_id>', methods=['GET'])
def details(game_id):
    #userResults = session.get('userResults', None)
    game_Data = api.requests_NameSpace("https://api.dccresource.com/api/games")
    gameInfo = srch.searchByID(game_Data, game_id)

    return render_template('sample/details.html', gameInfo=gameInfo)


@bp.route('/sample')  # URL Route
def index():  # Index.html

    game_Data = api.requests_NameSpace("https://api.dccresource.com/api/games")
    copiesPer = pfd.copiesPer_Dict(game_Data)

    return render_template('sample/index.html', copiesPer=copiesPer)

@bp.route('/sample/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


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
