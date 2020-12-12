from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


"""
@app.route('/hello')
def hello():
    return "Hello, World!"


@app.route('/index')
def index():
    return index.html
"""

