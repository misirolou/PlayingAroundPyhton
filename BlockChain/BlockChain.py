#Simple blockchain created following https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
#learning other methods to understand what is possible with python
#Also another way of gaining better knowledge around the craetion of blockchains and how they work

import hashlib
import json
from time import time
from uuid import uuid4
from textwrap import dedent

from flask import Flask
from flask import jsonify

#Class is responsible for managing the chain, storing transactions and contains some helper methods.
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #creating a genesis block
        self.new_block(previous_hash=1, proof=100)

#Creates a new block and adds it to the chain
#    param proof: <int> Proof given by the proof of work algorithm
#    param previous_hash: (Optional) <str> Hash of previous block
#    return: <dict> New Block

    def new_block(self, proof,previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        #reset current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

#Creates new transaction to be processed into next mined block
#    param sender: <str> Address to sender
#    param recipient: <str> Address to recipient
#    param amount: <int> Amount 
#    :return: <int> Index the block that will hold transaction

    def new_tranaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1
    
    #Returns the last block in the chain
    @property
    def last_block(self):
        return self.chain[-1]


    
#Creates a SHA-256 hash of a block
#    param block: <dict> a block
#    reurn: <str>

    @staticmethod
    def hash(block):
#Must make sure Dictionary is Ordered or else we´ll have inconsistent hashes
        block_string = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Simple Proof of work Algortihm
#find a number p' such that hash(pp') contains leading 4 zeroes, where p is previous p'
#p is the previous proof, and p' is the new proof
#   param last_proof: <int>
#   return: <int>
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

#Validates the Proof: does hash(last_proof, proof) contain 4 leading zeroes?
#Its possible to add more zeroes but this would cause longer times to validate the proof
#   param last_proof: <int> Previous proof
#   param proof: <int> Current proof
#   return: <bool> true if correct, false if not
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

#instantiate the node
app = Flask(__name__)

#generate a globallt unique address for this node
node_identifier = str(uuid4()).replace('-','')

#Instantiate BlockChain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "Mining a  new block"

@app.route('/transactions/new', methods=['POST'])
def new_tranaction():
    return "Adding a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain' : blockchain.chain,
        'length' : len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

''' Example of what a single block would look like and what it should contain
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}'''

