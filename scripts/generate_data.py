import pandas as pd
import numpy as np
import os

# 1. Create a 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

print("⏳ Creating 1,000,000 bank transactions... this will take a few seconds.")

# 2. Number of rows
n_rows = 1_000_000

# 3. Generating the data
data = {
    # Unique ID for every transaction
    'transaction_id': np.arange(n_rows),
    
    # Random money amounts between $1 and $5,000
    'amount': np.random.uniform(1, 5000, n_rows).round(2),
    
    # Time of day (0 to 23 hours)
    'hour': np.random.randint(0, 24, n_rows),
    
    # The 'Target': 1 means Fraud, 0 means Safe
    # We set fraud at only 1% because theft is rare in real life
    'is_fraud': np.random.choice([0, 1], size=n_rows, p=[0.99, 0.01])
}

# 4. Save to a Table
df = pd.DataFrame(data)

# 5. Save to your 'data' folder as a CSV file
df.to_csv('data/transactions.csv', index=False)

print("✅ DONE! You now have a file with 1,000,000 rows in your 'data' folder.")