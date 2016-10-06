#! /bin/usr/python3

from flask import Flask, request, render_template, jsonify
import requests
import re, sys
from random import random
from bootstrapy import bootstrapy
import json

app = Flask(__name__)

@app.route('/test')
def test():
    modules = requests.get('http://koncentrator:80/module/list')
    modules = modules.json()
    list_modules = []
    list_wells = []
    content_panel = ""
    for m in modules:
        list_modules = list_modules + [{'interval': str(1000 * 10), 'function': (modules[m].replace('-', '_')) + '_func', 'url': m, 'id': modules[m]}]
        list_wells = list_wells + [bootstrapy.build_well('<div id="' + modules[m] + '">Loading...</div>')]
        content_panel += '<button id="' + modules[m] + '_button" type="button" class="btn btn-primary" style="width:100%">' + modules[m] + '</button>'
    return render_template("main.html", content="", modules=[])
    #return render_template("main.html", content=bootstrapy.build_side_panel(bootstrapy.build_well(content_panel), bootstrapy.build_grid(list_wells)), modules=list_modules)

@app.route('/module/list')
def list_modules():
    return requests.get('http://koncentrator:80/module/list').text

@app.route('/get_from_module/<module>')
def get_from_module(module):
    req = requests.get('http://koncentrator:80/module/{0}/content'.format(module))
    out = req.json()
    print(out)
    return out['content']

@app.route('/')
def main():
    return render_template("main.html", content=well_4x4, modules=[ping_module, random_module])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
