from flask import jsonify, Blueprint

api = Blueprint('api', __name__)

@api.route('/info/list/module')
def list_module():
    dict = {}
    dict['test'] = '657e4'
    return jsonify(dict)

@api.route('/info/koncentrator')
def info_koncentrator():
    settings = reader.Settings('config.yml')
    return jsonify(settings.get_content())

@api.route('/module/<string:module_id>/content')
def get_content(module_id):
    if module_id == '657e4':
        return '<html>Hello World from module</html>'
    else:
        return '<html>Error! Module not found</html>', 404
