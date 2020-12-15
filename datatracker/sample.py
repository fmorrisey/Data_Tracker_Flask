from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from datatracker.platformData import platformData as pfd
from datatracker.api import api

bp = Blueprint('sample', __name__)


@bp.route('/', methods=['GET'])
def search():
    return render_template('sample/search.html')


@bp.route('/search/results', methods=['GET', 'POST'])

def search_requests():
    search_term = request.form["input"]
    game_Data = api.requests_NameSpace("https://api.dccresource.com/api/games")
    copiesPer = pfd.copiesPer_Dict(game_Data)
    results = search()
    return render_template('results.html', res=results)


@bp.route('/test')
def test():
    return "All good!"


@bp.route('/sample')  # URL Route
def index():  # Index.html
    game_Data = api.requests_NameSpace("https://api.dccresource.com/api/games")
    copiesPer = pfd.copiesPer_Dict(game_Data)
    nintedoGames = pfd.NintendoAfter(game_Data, 2016)
    return render_template('sample/index.html', titles=publishers, copiesPer=copiesPer, nintedoGames=nintedoGames)

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
