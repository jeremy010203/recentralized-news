#! /bin/usr/python3

from flask import Flask
from config import reader
from view_api import view
from module_api import module

app = Flask(__name__)
app.register_blueprint(view.api)
app.register_blueprint(module.api)

@app.route('/hello-world')
def hello_world():
    return "<html>Hello World!</html>"

if __name__ == "__main__":
    settings = reader.Settings("config.yml")
    if "port" in settings.get_content():
        port = settings.get_content().port
    else:
        port = 80
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
