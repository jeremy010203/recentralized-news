from flask import Flask
from config import reader
from view_api import view
from module_api import module

app = Flask(__name__)
app.register_blueprint(view.api)
app.register_blueprint(module.api)

@app.route('/hello-world')
def hello_world():
    return "<html>Hello World</html>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

def add_module(module):
    global modules
    modules[module.module_id] = module

def get_modules():
    global modules
    return modules

def get_module(module_id):
    global modules
    if module_id in modules:
        return modules[module_id]
    else:
        return None
>>>>>>> [FIX] koncentrator port flask
