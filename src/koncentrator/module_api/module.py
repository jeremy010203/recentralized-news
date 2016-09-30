from flask import request, jsonify, Blueprint, current_app
from utils import utils
import requests

api = Blueprint('module', __name__)

global module_id
module_id = 0

@api.route('/module/register', methods=['POST'])
def register_module():
    dict = request.json 
    current_app.logger.debug("Got connection from: %s", dict['name'])
    module = Module(dict['name'])
    utils.add_module(module)
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

    def get_content(self):
        try:
            req = requests.get("http://{0}:{1}/content".format(self.module_name, "80"))
            if req.status_code == 200:
                return req.content
        except:
            utils.remove_module(self.module_id)
            return "<html>Error !</html>"
        utils.remove_module(self.module_id)
