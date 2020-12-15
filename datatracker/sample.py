from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from datatracker.platformData import platformData as pfd
from datatracker.api import api


bp = Blueprint('sample', __name__)

games = {
    'Electronic Arts': 1351,
    'Activision': 975,
    'Namco Bandai Games': 932,
    'Ubisoft': 921,
    'Konami Digital Entertainment': 832,
    'THQ': 715,
    'Nintendo': 703,
    'Sony Computer Entertainment': 683,
    'Sega': 639,
    'Take-Two Interactive': 413
}
publishers = []
games_released = []
test = []

for company, copies in games.items():
    publishers.append(company)
    games_released.append(copies)


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
