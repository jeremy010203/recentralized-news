#! /bin/usr/python3

from flask import Flask, jsonify
import requests
import time
import threading

app = Flask(__name__)

@app.route('/content')
def main():
    return "Hello world!"

def loop():
    while True:
        mod_id = dict['token']
        url = "http://koncentrator:80/module/" + mod_id + "/content"
        out = requests.post(url, json={"content":"<html>Hello World!</html>"})
        time.sleep(10)

if __name__ == '__main__':
    out = requests.post('http://koncentrator:80/module/register',
            json={"name":"hello-world-push","push":True,"expiration":5})
    dict = out.json()
    print(dict)
    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
    app.run(host='0.0.0.0', port=80, threaded=True)
