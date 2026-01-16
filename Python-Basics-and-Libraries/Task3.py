# Task 3: Load a CSV file with Pandas, clean it (handle missing values), and export a summary.
import pandas as pd

df = pd.read_csv('student_scores_missing.csv')
print("Original DataFrame:")
print(df)

print("\nInfo:") 
print(df.info())

# missing values
print("\nMissing Values in each column:")
print(df.isnull().sum())    


# #Seprate numeric and non-numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns
non_numeric_cols = df.select_dtypes(exclude=['number']).columns

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# For non-numeric columns, fill missing values with the mode
for col in non_numeric_cols:
    mode_value = df[col].mode()[0]
    df[col].fillna(mode_value, inplace=True)

print("\nCleaned DataFrame:")
print(df)

summary = df.describe(include='all')
print("\nSummary :")

print(summary)


