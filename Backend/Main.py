import hashlib
import json
from time import time

import requests

class BlockChain(object):

    def __init__(self):
        self.chain = []
        self.currentTransaction = []

        # Create the genesis block
        self.new_block(proof=100, previous_hash='1')

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.currentTransaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.currentTransaction = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        transfer_block = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }

        self.currentTransaction.append(transfer_block)
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
    
    # adding a PoW 
    @staticmethod
    def Validate_proof(proof, last_proof): 
        combined_string = f"{proof}{last_proof}".encode() # combines the proof and last_proof 
                                                            # as Strings 
        combined_string_guess= hashlib.sha256(combined_string).hexdigest()
        if combined_string_guess[:4] == '0000': 
            return combined_string_guess

    
    def Proof_of_Work(self, last_proof): 
        proof = 0;
        
        while not self.Validate_proof(proof, last_proof):
            proof += 1 
        return proof


    def validate_chain(self, chain): 
        last_block = chain[0]
        current_index = 1;
        
        while current_index < len(chain): 
            block = chain[current_index]
            
        
            if block['previous_hash'] != self.hash(last_block): 
                return False

            
            if not self.Validate_proof( block['proof'], last_block['proof']): 
            
                return False
   
            last_block = block 
            current_index +=1 
        return True

    def mine(self):
        if not self.currentTransaction: 
            return "No Transaction to mine"
        
        last_block = self.last_block 
        last_proof = last_block['proof']
        proof = self.Proof_of_Work(last_proof)
        
        previous_hash = self.hash(last_block)
        new_block = self.new_block(proof, previous_hash)
        return new_block


        
# test run 



blockchain = BlockChain() 

blockchain.new_transaction(sender ='Kishan',recipient="Kishan", amount= 300)

mined = blockchain.mine()
print(mined)
is_valid = blockchain.validate_chain(blockchain.chain)
print(f"Is This Block Chain Valid: {is_valid}")

''' 
block = BlockChain()
last_proof = block.last_block['proof']
proof = block.Proof_of_Work(last_proof)
block.new_block(proof)
print(block.new_block(proof= 123, previous_hash= 'abc'))
print(f"The last Proof: {proof}, New Proof: {last_proof}")
is_valid = block.validate_chain(block.chain)
print(f'Is this BlockChain valid?: {is_valid}')
'''