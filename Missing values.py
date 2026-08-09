import pandas as pd

# Load your dataset 
df = pd.read_excel(r"C:\Users\3601s\OneDrive\Desktop\STUDY MATERIAL\Sem - 2\Case study - 2\US CANDA TRADE 1 .xlsx")

# 1. Check if any values are missing
print("Any missing values in the dataset?")
print(df.isnull().values.any())

# 2. Count of missing values per column
print("\nMissing values per column:")
print(df.isnull().sum())

# 3. Percentage of missing values per column
print("\nPercentage of missing values per column:")
print((df.isnull().sum() / len(df)) * 100)

# Optional: Display rows with missing values
print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])
