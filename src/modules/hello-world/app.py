#! /bin/usr/python3

from flask import Flask, request, render_template, jsonify
import subprocess
import re, sys
from random import random
from bootstrapy import bootstrapy

app = Flask(__name__)

@app.route('/content')
def main():
    return "Hello world"

if __name__ == '__main__':
    out = subprocess.check_output(["curl", "-X","POST", "-H", "Content-Type: application/json", "-d", "{'name': 'hello-world'}", 'koncentrator:80/module/register']).decode('utf-8')
    print(str(out))
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
