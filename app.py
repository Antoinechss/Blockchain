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
    pass

@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    pass

@app.route("/chain", methods=["GET"])
def full_chain():
    full_chain = {"chain": blockchain.chain, "length": len(blockchain.chain)}
    return jsonify(full_chain), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)