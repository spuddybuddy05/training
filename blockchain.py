import hashlib

class NewBitcoin:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna sends 2.77 NBC to Mom"
t2 = "Amber sends 2.68 NBC to Dad"
t3 = "No you sends 6 NBC to Food"
t4 = "Pizza sends 9 NBC to Jean"
t5 = "Water sends 2 NBC to AK"
t6 = "Soda sends 1 NBC to LAY"

initial_block = NewBitcoin("Intial String", [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NewBitcoin(initial_block.block_hash, [t3,t4])
3
print(second_block.block_data)
print(second_block.block_hash)

third_block = NewBitcoin(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)