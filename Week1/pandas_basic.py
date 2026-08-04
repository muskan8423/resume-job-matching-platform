import pandas as pd

# Load the dataset
df = pd.read_csv("sample_dataset.csv")

print("===== RESUME DATASET =====")
print(df)

# Display first 5 rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Display dataset shape
print("\n===== DATASET SHAPE =====")
print(df.shape)

# Display column names
print("\n===== COLUMN NAMES =====")
print(df.columns)

# Display data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Check duplicate rows
print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())


# Features
features = df[["Skills", "Experience", "Education"]]

# Label
labels = df["Job_Role"]

print("\n===== FEATURES =====")
print(features)

print("\n===== LABELS =====")
print(labels)


# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Skills"] = df["Skills"].fillna("Not Specified")
df["Education"] = df["Education"].fillna("Not Specified")
df["Job_Role"] = df["Job_Role"].fillna("Not Specified")

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")