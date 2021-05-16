# -*- coding: utf-8 -*-

import flask
import requests

app = flask.Flask(__name__)

@app.route('/getids',methods = ['OPTIONS'])
def getidsOption():
    response = flask.make_response("proxy ok", 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

@app.route('/getids',methods = ['POST', 'OPTIONS'])
def getids():
    print("-----------------")
    print(flask.request.json['type'])
    payload = flask.request.json
    r = requests.post('https://api.mangadex.org/legacy/mapping', json=payload)
    print (r.text)

    response = flask.make_response(r.text, r.status_code)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
