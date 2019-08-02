import flask
import urllib.request
import os.path
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False


@app.route('/', methods=['POST'])
def home():
    content=request.json
    print(content['url'])
    filepath = content['name'] + '/' + content['name'] + '_' + content['version']
    if not os.path.isdir(content['name']):
        os.makedirs(content['name'])
    urllib.request.urlretrieve(content['url'], filepath)
    return "OK!\n"

if __name__ == '__main__':
    app.run(port=5555)
