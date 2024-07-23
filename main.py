from datetime import datetime
from hashlib import sha256


class Block:
    def __init__(self,index,author,timestamp,data,previous_hash):
        self.index = index
        self.author = author
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.create_hash()

    def create_hash(self):
        hash_str = self.index+self.author+self.data+str(datetime.now())
        return sha256(hash_str.encode()).hexdigest()

class blockchain:
    def __init__(self):
        self.chain = [self.genesis_block()]

    def genesis_block(self):
        return Block('0',"Proginator",datetime.now(),"Initialization","0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self,new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.create_hash()
        self.chain.append(new_block)

chain = blockchain()

chain.add_block(Block("1","Steven Smith",datetime.now(),"Transaction 1",""))
chain.add_block(Block("2","Deborah Jones",datetime.now(),"Transaction 2",""))
chain.add_block(Block("3","Joseppy Gorgonzoli",datetime.now(),"Transaction 3",""))

for link in chain.chain:
    print("Block index: %s"%link.index)
    print("Block data: %s"%link.data)
    print("Block author: %s"%link.author)
    print("Block hash: %s"%link.hash)
    print("Block timestamp: %s"%link.timestamp)
    print("Previous hash: %s"%link.previous_hash)
    print("\n")


