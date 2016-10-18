from flask import jsonify, Blueprint, request
from utils import utils
import uuid
import time

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

@api.route('/module/<string:module_id>/content', methods=['POST'])
def post_content(module_id):
    module = utils.get_module(module_id=module_id)
    view = utils.get_view(request.json['token'])
    answer = {}
    if view is None:
        answer['changed'] = True
        answer['data'] = "You are not able to do this"
        answer['error'] = True
        return jsonify(answer), 403
    if module is None:
        answer['changed'] = True
        answer['data'] = "This id does not refer any module"
        answer['error'] = True
        return jsonify(answer), 404
    answer['error'] = False
    if module.push_method:
        content = module.get_last_content()
        if content is None:
            answer['changed'] = False
            answer['data'] = "Module has not pushed anything yet"
            answer['error'] = True
            return jsonify(answer), 404
        elif content.is_expired():
            answer['changed'] = False
            answer['data'] = "Content for this module has expired"
            answer['error'] = True
            utils.remove_module(module_id)
            return jsonify(answer), 404
        elif module_id in view.polled:
            if view.polled[module_id] < content.receive_time:
                answer['changed'] = True
                answer['data'] = content.raw_content
                view.polled[module_id] = int(time.time())
        else:
            view.polled[module_id] = int(time.time())
            answer['changed'] = True
            answer['data'] = content.raw_content
    else:
        content = module.get_content()
        answer['content'], answer['changed'] = module.get_content()
        answer['error'] = not answer['changed']
        if answer['error']:
            answer['data'] = "Module has disconnected"
            return jsonify(answer), 404
    return jsonify(answer)

@api.route('/module/<string:module_id>/content', methods=['GET'])
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

@api.route('/view/register')
def register_view():
    view = View()
    answer = {}
    answer['token'] = view.token
    utils.add_view(view)
    return jsonify(answer)

class View:
    token = None
    polled = None

    def __init__(self):
        self.token = uuid.uuid4().hex
        self.polled = {}
