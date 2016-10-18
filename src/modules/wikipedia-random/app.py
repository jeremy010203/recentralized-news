#! /bin/usr/python3

from flask import Flask, jsonify
import requests
import time
import threading
from wiki import wiki

app = Flask(__name__)

@app.route('/content')
def main():
    return wiki.get_random_page()

def loop():
    while True:
        mod_id = dict['token']
        url = "http://koncentrator:80/module/content"
        out = requests.post(url, json={"token":mod_id, "content":wiki.get_random_page()})
        time.sleep(600)

if __name__ == '__main__':
    out = requests.post('http://koncentrator:80/module/register',
            json={"name":"wikipedia-random","push":True,"expiration":1000})
    dict = out.json()
    print(dict)
    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
    app.run(host='0.0.0.0', port=80, threaded=True)
