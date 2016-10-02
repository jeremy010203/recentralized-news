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
    if 'host' in settings.get_settings():
        host = settings.get_settings()['host']
    else:
        host = '0.0.0.0'
    if 'port' in settings.get_settings():
        port = settings.get_settings()['port']
    else:
        port = 80
    app.run(host=host, port=port, debug=True, threaded=True)
