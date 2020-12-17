from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint, session
from datatracker.platformData import platformData as pfd
from datatracker.api import api
from datatracker.search import search as srch
from datatracker.salesData import salesData as sds
import json

bp = Blueprint('sample', __name__)

#APIRequests_for data
game_Data = api.requests_NameSpace("https://api.dccresource.com/api/games")
copiesPer = pfd.copiesPer_Dict(game_Data)
salesPer = sds.salesPer_Global(game_Data, 2013, 2020)


@bp.route('/')  # URL Route
def home():  # Index.html

    return render_template('/sample/home.html')

@bp.route('/sample')  # URL Route
def index():  # Index.html

    return render_template('/sample/index.html', copiesPer=copiesPer)

@bp.route('/sample/sales')  # URL Route
def sales():  # Index.html

    return render_template('/sample/sales.html', salesPer=salesPer)

@bp.route('/analysis')  # URL Route
def analysis():  # analysis.html

    return render_template('/sample/analysis.html')

"""
@bp.route('/sample/search', methods=['GET'])
def search():
    return render_template('/sample/search.html')
"""

@bp.route('/sample/results', methods=['GET', 'POST'])
def search_requests():
    search_term = request.form["input"]
    results, hits = srch.searchByName(game_Data, search_term)

    return render_template('/sample/results.html', res=results, hits=hits)


@bp.route('/sample/details/<game_id>', methods=['GET'])
def details(game_id):

    gameInfo = srch.searchByID(game_Data, game_id)

    return render_template('/sample/details.html', gameInfo=gameInfo)






