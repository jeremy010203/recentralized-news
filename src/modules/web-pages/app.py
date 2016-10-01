#! /bin/usr/python3

from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/content')
def main():
    return "<iframe src='http://epita.fr' width='100%' height='100%'></iframe>"

if __name__ == '__main__':
    out = subprocess.check_output(["curl", "-X","POST", "-H", "Content-Type: application/json", "-d", '{"name": "web-pages"}', 'koncentrator:80/module/register']).decode('utf-8')
    print(str(out))
    app.run(host='0.0.0.0', port=80, threaded=True)
