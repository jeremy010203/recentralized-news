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
    for m in modules:
        list_modules = list_modules + [{'interval': '5000', 'function': 'hello_func', 'url': m, 'id': modules[m]}]
        well = bootstrapy.build_well('<span name="' + modules[m] + '">Loading...</span>')
        well_2x2 = bootstrapy.build_2x2_grid(well, well, well, well)
        well_4x4 = bootstrapy.build_2x2_grid(well_2x2, well_2x2, well_2x2, well_2x2)
        well_8x8 = bootstrapy.build_2x2_grid(well_4x4, well_4x4, well_4x4, well_4x4)

    return render_template("main.html", content=well_8x8, modules=list_modules)

@app.route('/get_from_module/<module>')
def get_from_module(module):
    out = subprocess.check_output(["curl", 'koncentrator:80/module/' + module + '/content']).decode('utf-8')
    return out

@app.route('/')
def main():
    return render_template("main.html", content=well_4x4, modules=[ping_module, random_module])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
