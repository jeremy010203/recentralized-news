#! /bin/usr/python3

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/content')
def main():
    return "Hello world!"

if __name__ == '__main__':
    out = requests.post('http://koncentrator:80/module/register', json={"name":"hello-world","push":True,"expiration":1})
    print(out.raw)

    out = requests.post('http://koncentrator:80/module/0/content', json={"content":"<html>Hello World!</html>"})
    print(out.raw)
    app.run(host='0.0.0.0', debug=True, port=80, threaded=True)
