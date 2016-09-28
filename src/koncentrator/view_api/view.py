from flask import jsonify, Blueprint
import app

api = Blueprint('api', __name__)

@api.route('/info/list/module')
def list_module():
    dict = {}
    modules = app.get_modules()
    for module in modules:
        dict[module] = modules[module].module_name
    return jsonify(dict)

@api.route('/info/koncentrator')
def info_koncentrator():
    settings = reader.Settings('config.yml')
    return jsonify(settings.get_content())

@api.route('/module/<string:module_id>/content')
def get_content(module_id):
    module = app.get_module(module_id)
    if module is not None:
        return module.module_name
    else:
        return "<html>No module found</html>"
