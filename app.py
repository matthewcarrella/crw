from flask import Flask, jsonify, request
import requests
app = Flask(__name__)


messages = ['first']

@app.route('/test', methods=['POST'])
def test():
    values = request.get_json()
    message = values["message"]
    messages.append(message)
    response_message = {'response': messages}
    return jsonify(response_message)

@app.route('/')
def hello_world():
    return 'Hello, World!'
