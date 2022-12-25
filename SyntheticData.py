import random
import string
import numpy as np

# Set the number of rows to generate
n_rows = 1000

# Generate the data rows
data = []
for i in range(n_rows):
    # Generate a random Ethereum address
    address = '0x' + ''.join(random.choices(string.hexdigits, k=40))
    
    # Generate random values for the other features
    volume = np.random.uniform(low=0, high=1e6)
    dapp_transactions = np.random.randint(low=0, high=100)
    matching_transactions = np.random.randint(low=0, high=100)
    age = np.random.randint(low=0, high=10)
    reviews = np.random.randint(low=0, high=100)
    
    # Append the data row to the list
    data.append([address, volume, dapp_transactions, matching_transactions, age, reviews])

# Convert the data to a NumPy array
data = np.array(data)