from flask import Flask
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ping')
def ping():
    try:
        out = subprocess.check_output(["ping", "-c", "1", 'google.fr']).decode('utf-8')
        regex = re.compile(r'time=([0-9]*).')
        res = 0
        count = 0
        for m in re.findall (regex, out):
            count = count + 1
            res += ixent(m)
        return out + '<br/>moy = '+ str(res / count) + 'ms'
    except:
        return 'ERROR: Timeout...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
