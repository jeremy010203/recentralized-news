from flask import jsonify, Blueprint
from utils import utils

api = Blueprint('api', __name__)

@api.route('/info/list/module')
def list_module():
    dict = {}
    modules = utils.get_modules()
    for module_key in modules:
        dict[module_key] = modules[module_key].module_name
    return jsonify(dict)

@api.route('/info/koncentrator')
def info_koncentrator():
    settings = reader.Settings('config.yml')
    return jsonify(settings.get_content())

@api.route('/module/<string:module_id>/content')
def get_content(module_id):
    module = utils.get_module(module_id)
    if module is not None:
        return module.get_content()
    else:
        return "<html>No module found</html>"
