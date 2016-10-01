#! /bin/usr/python3

from flask import Flask
import subprocess
import xmltodict

app = Flask(__name__)

@app.route('/content')
def main():
    out = subprocess.check_output(["curl", "www.lemonde.fr/rss/une.xml"]).decode('utf-8')
    doc = xmltodict.parse(out)
    res = ""
    for item in doc['rss']['channel']['item']:
        res = res + "<a href='" + str(item['link']) + "'>"+ str(item['title']) + '</a><br />'
    return res

if __name__ == '__main__':
    out = subprocess.check_output(["curl", "-X","POST", "-H", "Content-Type: application/json", "-d", '{"name": "web-pages"}', 'koncentrator:80/module/register']).decode('utf-8')
    print(str(out))
    app.run(host='0.0.0.0', port=80, threaded=True)
