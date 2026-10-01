import pandas as pd

# ==========================================
# TASK 1: DATA CLEANING AND PREPROCESSING
# ==========================================

# Load the raw dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("Original Dataset Shape:", df.shape)

# ------------------------------------------
# Check missing values
# ------------------------------------------

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# ------------------------------------------
# Check duplicate rows
# ------------------------------------------

print("\nDuplicate Rows Before Cleaning:")
print(df.duplicated().sum())

# ------------------------------------------
# Clean column names
# ------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

print("\nCleaned Column Names:")
print(df.columns.tolist())

# ------------------------------------------
# Remove duplicate rows
# ------------------------------------------

df = df.drop_duplicates()

# ------------------------------------------
# Convert date column
# ------------------------------------------

df["dt_customer"] = pd.to_datetime(
    df["dt_customer"],
    errors="coerce"
)

# ------------------------------------------
# Convert income to numeric
# ------------------------------------------

df["income"] = pd.to_numeric(
    df["income"],
    errors="coerce"
)

# ------------------------------------------
# Handle missing income values
# ------------------------------------------

df["income"] = df["income"].fillna(
    df["income"].median()
)

# ------------------------------------------
# Final validation
# ------------------------------------------

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Data Types:")
print(df.dtypes)

# ------------------------------------------
# Save cleaned dataset
# ------------------------------------------

df.to_csv(
    "customer_personality_cleaned.csv",
    index=False
)

print("\nCleaning completed successfully!")
print("File created: customer_personality_cleaned.csv")