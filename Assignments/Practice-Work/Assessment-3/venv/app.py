from flask import Flask, request, render_template, redirect, flash, session, jsonify
import requests
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


toolbar = DebugToolbarExtension(app)

@app.route('/', methods=['GET'])
def test():
    return render_template('http://api.exchangerate.host/live?access_key=ea15dd788a5cb2d3800d4d987863f31e&format=1')