import flask
import urllib.request
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False


@app.route('/', methods=['POST'])
def home():
    content=request.json
    print(content['url'])
    filename = content['name'] + '_' + content['version']
    urllib.request.urlretrieve(content['url'], filename)
    return "OK!\n"

if __name__ == '__main__':
    app.run(port=5555)
