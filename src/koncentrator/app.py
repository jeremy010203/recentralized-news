from flask import Flask, jsonify
from config import reader

app = Flask(__name__)

@app.route('/hello-world')
def hello_world():
    return "<html>Hello World</html>"

@app.route('/info/list/module')
def list_module():
    dict = {}
    dict['test'] = '657e4'
    return jsonify(dict)

@app.route('/info/koncentrator')
def info_koncentrator():
    settings = reader.Settings('config.yml')
    return jsonify(settings.get_content())

@app.route('/modules/<int:id>/content')
def get_content():
    if id == '657e4':
        return '<html>Hello World from module</html>'
    else:
        return '<html>Error! Module not found', 404
