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
    app.run()
