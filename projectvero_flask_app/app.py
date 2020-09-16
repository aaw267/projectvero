from flask import Flask, jsonify
import requests
import hashlib
import json
from time import time  #this is pulling the lower object time from the time package
from uuid import uuid4
from textwrap import dedent
from projectvero_flask_app.api.blockchain import Blockchain

app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return 'FUCK YOU'


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "FUCK YOU x2"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
