from flask import Flask
from ensure import ensure

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><b>Hello</b>, World!</p>"

@app.route("/hello")
def hello_guy(req):
    name = req.args.get('name', 'Guy')
    return f"<p><i>Hello</i>, {ensure(name)}!</p>"
