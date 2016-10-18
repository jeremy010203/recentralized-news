from flask import request, jsonify, Blueprint, current_app
from utils import utils
from . import content
import uuid
import requests

api = Blueprint('module', __name__)

global module_id
module_id = 0

@api.route('/module/register', methods=['POST'])
def register_module():
    dict = request.json
    current_app.logger.debug(request.json)
    current_app.logger.debug("Got connection from: %s", dict['name'])
    module = Module(dict)
    utils.add_module(module)
    answer = {}
    answer['success'] = True
    if 'push' in dict and bool(dict['push']):
        current_app.logger.debug("The module '%s' (%d)(%s) is a push module", dict['name'], int(module.module_id), module.private_token)
        answer['token'] = module.private_token
    return jsonify(answer)

@api.route('/module/content', methods=['POST'])
def register_content():
    dict = request.json
    token = dict['token']
    module = utils.get_module(token=token)
    answer = {}
    if module is not None:
        current_app.logger.debug("Got content for module '%s':\n%s", module.module_id, request.json)
        ct = content.Content(module.expiration, dict['content'])
        module.cache_content(ct)
        answer['success'] = True
    else:
        answer['success'] = False
    return jsonify(answer)

class Module:
    module_name = None
    module_id = None
    push_method = False
    contents = None
    expiration = None
    private_token = None

    def __init__(self, settings):
        global module_id
        self.module_id = str(module_id)
        module_id += 1
        self.module_name = settings['name']
        if 'push' in settings:
            self.private_token = uuid.uuid4().hex
            self.contents = []
            self.push_method = settings['push']
            if "expiration" in settings:
                self.expiration = settings['expiration']
            else:
                self.expiration = 300

    def get_last_content(self):
        if self.push_method and len(self.contents) > 0:
            return self.contents[-1]
        return None

    def get_content(self):
        answer = {}
        if self.push_method:
            if len(self.contents) > 0:
                content = self.contents[-1]
                if not content.is_expired():
                    return content.raw_content, True
        try:
            req = requests.get("http://{0}:{1}/content".format(self.module_name, "80"))
        except:
            req = None
        if req is not None and req.status_code == 200:
            return req.text, True
        utils.remove_module(self.module_id)
        return "Module disconnected", False

    def cache_content(self, content):
        self.contents.append(content)
