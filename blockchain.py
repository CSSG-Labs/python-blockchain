import hashlib
import json
from time import time


class Blockchain():
    def __init__(self):
        self.chain = [] # List to hold blocks
        self.current_transactions = [] # List to hold transactions
    
    def new_block(self, proof, previous_hash=None):
        # Create a new block and add to blockchain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        # Append block to chain and return block
        self.chain.append(block)
        return block

    def new_transaction(self):
        # Add new transaction to list of transactions
        pass

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block
        :param block: <dict> block
        :return: <str>
        """

        # Convert block dict to json string using json.dumps and sort keys for consistency across
        # hashes and encode json string using encode method 
        block_string = json.dumps(block, sort_keys=True).encode()

        # Hash string using sha256 and apply hexdigest, then return
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last block in the chain
        return self.chain[-1]