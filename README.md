<h1 align="center">Blockchain — Python Implementation from Scratch</h1>

<p align="center">
  <em>
    A simple educational implementation of a blockchain to understand its core mechanisms.
  </em>
</p>

---

## Overview

This project is a **basic blockchain implementation built from scratch in Python**.
It simulates how a real blockchain operates at a fundamental level, focusing on
block creation, hashing, transactions, and proof of work.

The goal is purely **educational**: understanding the internal logic behind
blockchains rather than building a production-ready system.

---

## Core Features

- Creation and storage of blocks linked together by cryptographic hashes  
- Addition of transaction requests before block mining  
- Proof of Work (PoW) algorithm for block mining  
- Chain validation through hash consistency  

---

## Blockchain Mechanics

<img width="2000" height="2000" alt="How-to-Build-A-Blockchain-In-Python" src="https://github.com/user-attachments/assets/33e984cd-ab32-4863-b456-ea3279278c51" />


### Block Structure

Each block contains:
- A list of transactions  
- A timestamp  
- A proof (result of the Proof of Work)  
- The hash of the previous block  

### Hashing

- Hash algorithm: **SHA-256**
- Hash function can be tested here:  
  https://emn178.github.io/online-tools/sha256.html

---

## Proof of Work Rule

To mine a block, the miner must find an integer `proof` such that:
SHA256(str(previous_proof) + str(proof)) starts with: 0000

This constraint ensures computational effort and simulates mining difficulty.

---

## API & Flask Integration

The blockchain is exposed via a **Flask API**, allowing interaction through HTTP endpoints.

### Available Interactions

- Submit new transactions  
- Mine new blocks (with mining rewards)  
- Retrieve the full blockchain  

---

## Running the Project

When executed, the Flask server runs by default on: http://0.0.0.0:5001


You can interact with the blockchain using tools such as `curl`, Postman,
or directly from a browser.

---

## Purpose

This project is intended as a **learning exercise** to understand:
- Blockchain data structures  
- Hash-based linking  
- Proof of Work mechanisms  
- Basic API interaction with a distributed ledger  




