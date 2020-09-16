from flask import Flask
import requests

from projectvero_flask_app.api.blockchain import Blockchain

app = Flask(__name__)

connor = Blockchain()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
