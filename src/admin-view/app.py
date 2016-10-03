#! /bin/usr/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "<html>Admin view</html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
