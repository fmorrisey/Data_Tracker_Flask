from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
es = Elasticsearch('10.0.1.10', port=9200)

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

