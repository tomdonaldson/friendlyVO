import os
from flask import Flask, request

from query import query
from ingest import ingest

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! I can deploy automatically :)'

app.register_blueprint(query, url_prefix='/query')

app.register_blueprint(ingest, url_prefix='/images')
