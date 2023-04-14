import pandas as pd

# Take user input for balance sheet items
assets = float(input("Enter total assets: "))
liabilities = float(input("Enter total liabilities: "))
equity = float(input("Enter total equity: "))

# Create balance sheet table
data = {'Category': ['Assets', 'Liabilities', 'Equity'],
        'Amount': [assets, liabilities, equity]}
balance_sheet = pd.DataFrame(data)

# Take user input for projected income statement items
revenue = float(input("Enter projected revenue: "))
expenses = float(input("Enter projected expenses: "))
net_income = revenue - expenses

# Create projected income statement table
data = {'Category': ['Revenue', 'Expenses', 'Net Income'],
        'Amount': [revenue, expenses, net_income]}
projected_income_statement = pd.DataFrame(data)

# Take user input for ratio analysis items
current_assets = float(input("Enter current assets: "))
current_liabilities = float(input("Enter current liabilities: "))
current_ratio = current_assets / current_liabilities

# Create ratio analysis table
data = {'Ratio': ['Current Ratio'],
        'Value': [current_ratio]}
ratio_analysis = pd.DataFrame(data)

# Take user input for projected cash flow statement items
operating_cash_flow = float(input("Enter operating cash flow: "))
investing_cash_flow = float(input("Enter investing cash flow: "))
financing_cash_flow = float(input("Enter financing cash flow: "))
net_cash_flow = operating_cash_flow + investing_cash_flow + financing_cash_flow

# Create projected cash flow statement table
data = {'Category': ['Operating Cash Flow', 'Investing Cash Flow', 'Financing Cash Flow', 'Net Cash Flow'],
        'Amount': [operating_cash_flow, investing_cash_flow, financing_cash_flow, net_cash_flow]}
projected_cash_flow_statement = pd.DataFrame(data)

# Take user input for fixed assets calculation items
fixed_assets_cost = float(input("Enter fixed assets cost: "))
accumulated_depreciation = float(input("Enter accumulated depreciation: "))
net_fixed_assets = fixed_assets_cost - accumulated_depreciation

# Create fixed assets calculation table
data = {'Category': ['Fixed Assets Cost', 'Accumulated Depreciation', 'Net Fixed Assets'],
        'Amount': [fixed_assets_cost, accumulated_depreciation, net_fixed_assets]}
fixed_assets_calculation = pd.DataFrame(data)

# Display all tables
print("Balance Sheet")
print(balance_sheet)
print("\nProjected Income Statement")
print(projected_income_statement)
print("\nRatio Analysis")
print(ratio_analysis)
print("\nProjected Cash Flow Statement")
print(projected_cash_flow_statement)
print("\nFixed Assets Calculation")
print(fixed_assets_calculation)