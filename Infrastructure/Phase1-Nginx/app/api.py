from flask import Flask , request
import sys #for printing in log console

app = Flask(__name__)


@app.route('/static')
def games():
    return 'wrong! load /static directory'

@app.route('/mobile')
def mobile():
    return 'This is mobile version'

@app.route('/limit')
def limit():
    return 'This is limit zone!'

@app.route('/endpoint1')
def endpoint1():
    return 'This is endpoint1'

@app.route('/endpoint2')
def endpoint2():
    return 'This is endpoint2'
