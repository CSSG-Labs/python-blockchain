class Blockchain():
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
    def new_block(self):
        # Create a new block and add to blockchain
        pass

    def new_transaction(self):
        # Add new transaction to list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # Returns the last block in the chain
        pass