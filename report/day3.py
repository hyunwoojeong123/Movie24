import hashlib

class Block:
    def __init__(self,_data,_prevhash,_nonce = 0):
        self.data = _data
        self.prevhash = _prevhash
        tempnonce = _nonce
        temphash = hashlib.sha256(self.data.encode() + str(tempnonce).encode()).hexdigest()
        if _data != 'Genesis Block':
            while temphash[:5] != '00000':
                tempnonce += 1
                temphash = hashlib.sha256(self.data.encode() + str(tempnonce).encode()).hexdigest()
        self.nonce = tempnonce
        self.hash = temphash
        # print(type(self.hash))
    def print(self):
        print('nonce:', self.nonce)
        print('data:', self.data)
        print('prevhash:', self.prevhash)
        print('hash:', self.hash)
        print()

class Chain:
    def __init__(self):
        self.chain = []

    def generate_block(self):
        if len(self.chain) == 0:
            self.chain.append(Block('Genesis Block', ''))
        else:
            prevhash = self.chain[len(self.chain)-1].hash
            self.chain.append(Block(str(len(self.chain)+1)+'nd',prevhash))
        self.chain[len(self.chain)-1].print()

# b1 = Block('Genesis Block', '')
# b1.print()
# b2 = Block('2nd', b1.hash)
# b2.print()
# b3 = Block('3nd', b2.hash)
# b3.print()

c = Chain()
for _ in range(3):
    c.generate_block()