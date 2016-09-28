from flask import request, jsonify, Blueprint, current_app
import app

api = Blueprint('module', __name__)

global module_id
module_id = 0

@api.route('/module/register', methods=['POST'])
def register_module():
    dict = request.json 
    current_app.logger.debug("Got connection from: %s", dict['name'])
    module = Module(dict['name'])
    app.add_module(module)
    answer = {}
    answer['success'] = True
    return jsonify(answer)

class Module:
    module_name = None
    module_id = 0
    def __init__(self, name):
        global module_id
        self.module_id = str(module_id)
        module_id += 1
        self.module_name = name
