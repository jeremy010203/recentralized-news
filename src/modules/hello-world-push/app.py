#! /bin/usr/python3

from flask import Flask, jsonify
import requests
import time

if __name__ == '__main__':
    out = requests.post('http://koncentrator:80/module/register',
            json={"name":"hello-world-push","push":True,"expiration":5})
    dict = out.json()

    while True:
        mod_id = dict['id']
        url = "http://koncentrator:80/module/" + mod_id + "/content"
        out = requests.post(url, json={"content":"<html>Hello World!</html>"})
        time.sleep(10)
