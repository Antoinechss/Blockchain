# Blockchain
Building a simple Blockchain from scratch in Python


This is my implementation of a basic blockchain - from scratch. 
It simulates how a real blockchain works at a fundamental level

Functions : 

* Create and store blocks that are linked together by hashes
* Add transactions requests before mining a block
* Run a proof of work algorithm to mine a new block

I used Flask to interact with the blockchain with API endpoints. 
Interactions : 
* Post new transactions
* Mine blocks (and get rewarded for it)
* See the full chain

Content of each block :  
Each block contains: a list of transactions, a timestamp, a proof (result of the PoW), the hash of previous block 

Hash algorithm = SHA-256 run it here : https://emn178.github.io/online-tools/sha256.html


Mining rule : find the proof (int) so that the hash of the previous proof + your proof starts with 0000.


When running, by default, the Flask server will run on: http://0.0.0.0:5001

