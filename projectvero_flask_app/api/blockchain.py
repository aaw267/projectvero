
# author: @alexwerner
import hashlib
import json
from time import time  #this is pulling the lower object time from the time package
from uuid import uuid4

class Blockchain(object):
    def __init__(self):
        self.chain = [] #[] is an empty list - lists are the best part of python
        self.current_transactions = []
        self.new_block(1, 100)

    def new_block(self, previous_hash = None, proof):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recepient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recepient': recepient,
            'amount': amount
            })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode() #takes the block dictionary and encodes it into a binary string which has the keys sorted alphabetically
        return hashlib.sha256(block_string).hexdigest() #Creates a 256 bit hash of the block string

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"
