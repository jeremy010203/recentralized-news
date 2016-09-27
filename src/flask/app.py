from flask import Flask
import subprocess
import re

app = Flask(__name__)

def build_2x2_grid(c1, c2, c3, c4):
    return build_container (build_row (build_col_md(c1, 6) + build_col_md(c2, 6)) + build_row (build_col_md(c3, 6) + build_col_md(c4, 6)))

def build_container(content):
    return '<div class="container-fluid">' + content + '</div>'

def build_col_md(content, nb):
    return '<div class="col-md-' + str(nb) + '">'+ content + '</div>'

def build_row(content):
    return '<div class="row">'+ content + '</div>'

def build_html(content):
    return '''<!DOCTYPE html>
                <html lang="en">
                <head>
                  <meta charset="utf-8">
                  <meta name="viewport"
                     content="width=device-width, initial-scale=1, user-scalable=yes">
                  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
                  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
                </head>
                <body>''' + content + '</body></html>'

@app.route('/')
def hello_world():
    return build_html(build_2x2_grid(build_2x2_grid("hello2", "hello2", "hello2", "hello2"), build_2x2_grid("hello2", "hello2", "hello2", "hello2")
        , build_2x2_grid("hello2", "hello2", "hello2", "hello2"), build_2x2_grid("hello2", "hello2", "hello2", "hello2")))

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
