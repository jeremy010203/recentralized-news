from flask import jsonify, Blueprint
from utils import utils

api = Blueprint('api', __name__)

@api.route('/info/koncentrator')
def info_koncentrator():
    settings = reader.Settings('config.yml')
    return jsonify(settings.get_content())

@api.route('/module/list')
def list_module():
    dict = {}
    modules = utils.get_modules()
    for module_key in modules:
        dict[module_key] = modules[module_key].module_name
    return jsonify(dict)

@api.route('/module/<string:module_id>/content')
def get_content(module_id):
    answer = {}
    answer['id'] = module_id
    module = utils.get_module(module_id=module_id)
    if module is not None:
        answer['content'], answer['success'] = module.get_content()
        return jsonify(answer)
    else:
        answer['success'] = False
        answer['error'] = "This id does not refer any module"
        return jsonify(answer), 404
