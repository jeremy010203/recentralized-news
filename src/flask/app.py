#! /bin/usr/python3

from flask import Flask, request, render_template, jsonify
import subprocess
import re, sys
from random import random
from bootstrapy import bootstrapy
import json

app = Flask(__name__)

@app.route('/test')
def test():
    modules = json.loads(subprocess.check_output(["curl", 'koncentrator:80/info/list/module']).decode('utf-8'))
    list_modules = []
    list_wells = []
    for m in modules:
        list_modules = list_modules + [{'interval': str(1000 * 10), 'function': (modules[m].replace('-', '_')) + '_func', 'url': m, 'id': modules[m]}]
        list_wells = list_wells + [bootstrapy.build_well('<span name="' + modules[m] + '">Loading...</span>')]

    return render_template("main.html", content=bootstrapy.build_grid(list_wells), modules=list_modules)

@app.route('/get_from_module/<module>')
def get_from_module(module):
    out = subprocess.check_output(["curl", 'koncentrator:80/module/' + module + '/content']).decode('utf-8')
    print(out)
    return out

@app.route('/')
def main():
    return render_template("main.html", content=well_4x4, modules=[ping_module, random_module])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
