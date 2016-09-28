from flask import Flask, request, render_template, jsonify
import subprocess
import re, sys
from random import random

app = Flask(__name__)

def build_2x2_grid(c1, c2, c3, c4):
    return build_container (build_row (build_col_md(c1, 6, 100) + build_col_md(c2, 6, 100), 50) + build_row (build_col_md(c3, 6, 100) + build_col_md(c4, 6, 100), 50))

def build_container(content):
    return '<div class="container-fluid">' + content + '</div>'

def build_col_md(content, nb, height):
    return '<div class="col-md-' + str(nb) + '" style="height: ' + str(height) + '%">'+ content + '</div>'

def build_row(content, height):
    return '<div class="row" style="height: ' + str(height) + '%">'+ content + '</div>'

def build_well(content):
    return '<div class="well" style="height: 90%">' + content + '</div>'

@app.route('/')
def main():
    well = build_well('<span name="random">' + get_random() + '</span>')
    well_2x2 = build_2x2_grid(well, well, well, well)
    well_4x4 = build_2x2_grid(build_well('<span name="ping">' + ping() + '</span>'), well_2x2, well_2x2, well_2x2)

    ping_module = {'interval': '1000', 'function': 'ping_func', 'url': '/ping', 'id': 'ping'}
    random_module = {'interval': '1000', 'function': 'random_func', 'url': '/random', 'id': 'random'}

    return render_template("main.html", content=well_4x4, modules=[ping_module, random_module])

@app.route('/hello_world')
def hello_world():
    return "Hello world"

@app.route('/random')
def get_random():
    return str(random())

@app.route('/ping')
def ping():
    try:
        out = subprocess.check_output(["ping", "-c", "1", 'google.fr']).decode('utf-8')
        regex = re.compile(r'time=([0-9]*).')
        res = 0
        count = 0
        for m in re.findall (regex, out):
            count = count + 1
            res += int(m)
        return out + '<br/>moy = '+ str(res / count) + 'ms'
    except Exception, e:
        return "Unexpected error:" + str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
