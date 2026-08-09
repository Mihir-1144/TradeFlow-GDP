import pandas as pd

# Load your dataset
df = pd.read_excel(r"C:\Users\3601s\OneDrive\Desktop\STUDY MATERIAL\Sem - 2\Case study - 2\US CANDA TRADE 1 .xlsx")  

# Select only numeric columns
numeric_cols = df.select_dtypes(include=['number'])

# Create a dictionary to store outlier info
outlier_summary = {}

# Loop through each numeric column
for col in numeric_cols.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    # Define bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Find outliers
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_count = outliers.shape[0]

    # Store in summary
    outlier_summary[col] = outlier_count

    # Optionally mark the outliers in the main DataFrame
    df[f'{col}_is_outlier'] = ((df[col] < lower_bound) | (df[col] > upper_bound))

# Print summary
print("Outlier counts by column:\n")
for col, count in outlier_summary.items():
    print(f"{col}: {count} outliers")

# Optional: Save the modified DataFrame with outlier flags
# df.to_csv('cleaned_with_outliers_flagged.csv', index=False)
