from flask import Flask, jsonify, request
import json
from uuid import uuid4
from blockchain import Blockchain

app = Flask(__name__)
# Generate a unique address for this node
node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route("/mine", methods=["GET"])
def mine():
    # Run POW Algo to compute new proof 
    last_block = blockchain.last_block
    last_proof = last_block["proof"]
    proof = blockchain.proof_of_work(last_proof)
    # Reward miner with a token 
    blockchain.new_transaction(sender="0",
                               recipient=node_identifier,
                               amount=1)
    # Add new block to the chain (forge new block)
    prev_hash = blockchain.hash(last_block)
    block = blockchain.new_block(prev_hash, proof)

    response = {"message": "new block forged",
                "index": block["index"],
                "transactions": block["transactions"],
                "proof": block["proof"],
                "previous_hash": block["previous_hash"]}
    return jsonify(response)

@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    values = request.get_json()
    index = blockchain.new_transaction(values["sender"], 
                                       values["recipient"], 
                                       values["amount"])
    response = {"message": f"transaction added to block {index}"}
    return jsonify(response)

@app.route("/chain", methods=["GET"])
def full_chain():
    response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)