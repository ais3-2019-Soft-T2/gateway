import urllib.request
import requests
import os.path
from flask import jsonify, request
import paho.mqtt.client as mqtt
import base64

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False


HOST = "174.138.24.232"
PORT = 1883

@app.route('/', methods=['POST'])
def home():
    print(request.json)
    content=request.json
    print(content['url'])
    filepath = content['name'] + '/' + content['name'] + '_' + content['version']
    if not os.path.isdir(content['name']):
        os.makedirs(content['name'])
    response = requests.get(content['url'])
    urllib.request.urlretrieve(content['url'], filepath)
    base64_response = base64.b64encode(response.content)
    mqtt_pub(base64_response)
    return "OK!\n"

def mqtt_pub(data):
    print('mqtt publish')
    client = mqtt.Client()
    client.connect(HOST, PORT, 60)
    client.publish("Topic", data, 2)
    client.loop_forever()


if __name__ == '__main__':
    app.run(port=5555)
