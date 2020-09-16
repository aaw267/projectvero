import hashlib
import json
from time import time

# author: @alexwerner
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(1, 100)

    def new_block(self, previous_hash, proof):
        pass

    def new_transaction(self):
        pass

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass
