import hashlib 
import json
from time import time 
from uuid import uuid4

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
        # create the genesis block 
        self.new_block(previous_hash=1, proof=100) 

    def new_block(self, previous_hash, proof):
        """
        create a new block in the chain 
        params: proof given by POW algo, hash of previous block
        """
        block = {"index": len(self.chain) + 1,
                 "timestamp": time(),
                 "transactions": self.current_transactions,
                 "proof": proof,
                 "previous_hash": previous_hash}
        
        self.current_transactions = [] # reset current list of transactions (from previous block)
        self.chain.append(block)
        return block 

    def new_transaction(self, sender, recipient, amount):
        """
        create a new transaction to go into the next mined Block 
        params: sender adress, recipient adress, amount 
        returns the index of the Block that will hold the transaction 
        """
        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount})
        return self.last_bloc["index"] + 1

    @staticmethod
    def hash(block):
        """
        create hash of block with SHA-256 algorithm 
        """
        # convert to json -> sort keys -> encode into bytes before hashing
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
    
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        hash = hashlib.sha256(guess).hexdigest()
        return hash[:4] == "0000"
    
    def proof_of_work(self, last_proof):
        """
        Simple POW algorithm : 
        find a number y such that hash(x*y) is led by 0000
        with x the previous proof and y the new proof 
        Compute all possible proofs until you find the right one (mining process)
        returns y 
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False: 
            proof += 1 
        return proof 
