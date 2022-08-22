import hashlib
import json


class Blockchain():
    def __init__(self):
        self.chain = [] # List to hold blocks
        self.current_transactions = [] # List to hold transactions
    
    def new_block(self):
        # Create a new block and add to blockchain
        pass

    def new_transaction(self):
        # Add new transaction to list of transactions
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

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