from flask import Flask, jsonify, request
from Test2 import BlockChain
from flask_cors import CORS
app = Flask(__name__)
blockchain = BlockChain()
CORS(app, resources={r"/*": {"origins": "https://block-chain-gules.vercel.app"}})


@app.route("/")
def home():
    return "<p>Hello world</p>"


@app.route("/mineblock", methods=['GET'])
def display_block():
    previous_block = blockchain.last_block
    previous_proof = previous_block['proof']
    proof = blockchain.Proof_of_Work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.new_block(proof, previous_hash)
    
    response = {
        'message': "The block is mined",
        'index': block['index'], 
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response)



@app.route("/validblock", methods=['GET'])
def valid_block():
    validation = blockchain.validate_chain(blockchain.chain)
    response = {"message": "The chain is valid" if validation else "The chain is not valid"}
    return jsonify(response), 200



@app.route("/getblock", methods=['GET'])
def get_block():
    responses = {
        'length': len(blockchain.chain), 
        'chain': blockchain.chain,
    }
    return jsonify(responses)



@app.route("/newtransaction", methods=["POST"])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(key in values for key in required):
        return "Missing values", 400
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f"Transaction will be added to Block {index}"}
    return jsonify(response), 201


@app.route("/registerNode", methods=["POST"])
def register_node():
    values = request.get_json()
    node = values.get('node')
    if node is None:
        return "Error: Please supply a valid node", 400
    blockchain.register_node(node)
    response = {
        "message": 'New node has been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route("/consensus", methods=["GET"])
def consensus():
    replaced = blockchain.resolve_conflicts()
    response = {
        'message': 'Our chain was replaced' if replaced else 'Our chain is authoritative',
        'new_chain': blockchain.chain
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)  # 
