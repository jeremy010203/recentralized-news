#! /bin/usr/python3

from flask import Flask, request, render_template, jsonify
import subprocess
import re, sys
from random import random
from bootstrapy import bootstrapy

app = Flask(__name__)

@app.route('/test')
def test():
    well = bootstrapy.build_well('<span name="hw">Loading...</span>')
    well_2x2 = bootstrapy.build_2x2_grid(well, well, well, well)
    well_4x4 = bootstrapy.build_2x2_grid(well_2x2, well_2x2, well_2x2, well_2x2)
    well_8x8 = bootstrapy.build_2x2_grid(well_4x4, well_4x4, well_4x4, well_4x4)

    hello_world_module = {'interval': '5000', 'function': 'hello_func', 'url': 'hello-world', 'id': 'hw'}

    return render_template("main.html", content=well_8x8, modules=[hello_world_module])

@app.route('/get_from_module/<module>')
def get_from_module(module):
    out = subprocess.check_output(["curl", 'koncentrator:80/' + module]).decode('utf-8')
    return out

@app.route('/')
def main():
    return render_template("main.html", content=well_4x4, modules=[ping_module, random_module])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
