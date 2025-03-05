# AI Transaction Categorization Script
import pandas as pd
import numpy as np

# Placeholder AI Categorization Logic
def categorize_transaction(amount):
    if amount < 0:
        return "Expense"
    else:
        return "Income"

# Example usage
transactions = pd.DataFrame({'Amount': [-200, 500, -50, 100]})
transactions['Category'] = transactions['Amount'].apply(categorize_transaction)

print(transactions)
