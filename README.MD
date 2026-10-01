# Task 1 – Data Cleaning and Preprocessing

## 📌 Project Overview

This project focuses on cleaning and preprocessing the **Customer Personality Analysis** dataset using **Python and Pandas**.

The raw dataset contains customer information that requires preprocessing before it can be used for further analysis and visualization.

## 🎯 Objective

The main objective is to:

* Identify and handle missing values
* Remove duplicate records
* Standardize column names
* Convert dates into a consistent format
* Fix incorrect data types
* Handle missing numerical values
* Export the cleaned dataset

## 🛠️ Tools and Technologies

* Python
* Pandas
* Visual Studio Code
* GitHub

## 📊 Dataset

**Dataset:** Customer Personality Analysis

**Input file:**

`marketing_campaign.csv`

**Output file:**

`customer_personality_cleaned.csv`

## 🧹 Data Cleaning Steps

The following preprocessing steps were performed:

1. Loaded the raw CSV dataset using Pandas.
2. Checked the dataset structure and data types.
3. Identified missing values using `isnull()`.
4. Identified duplicate records using `duplicated()`.
5. Standardized column names by converting them to lowercase and replacing spaces with underscores.
6. Removed duplicate rows using `drop_duplicates()`.
7. Converted `Dt_Customer` into a datetime format.
8. Converted `Income` into a numeric data type.
9. Handled missing income values using the median.
10. Performed final validation after cleaning.
11. Saved the cleaned dataset as a new CSV file.

## 📁 Project Structure

```text
Task-1-Data-Cleaning/
│
├── marketing_campaign.csv
├── customer_personality_cleaned.csv
├── data_cleaning.py
└── README.md
```

## 💻 How to Run

### 1. Install Pandas

Open the VS Code terminal and run:

```bash
pip install pandas
```

### 2. Run the Python script

Make sure `marketing_campaign.csv` and `data_cleaning.py` are in the same folder.

Run:

```bash
python data_cleaning.py
```

### 3. Output

After successful execution, the following file will be created:

```text
customer_personality_cleaned.csv
```

## 🔍 Key Pandas Functions Used

```python
pd.read_csv()
df.isnull()
df.duplicated()
df.drop_duplicates()
pd.to_datetime()
pd.to_numeric()
df.fillna()
df.to_csv()
```

## 📈 Result

The raw dataset was cleaned and transformed into a structured dataset suitable for further data analysis and visualization.

The cleaned dataset contains standardized column names, corrected data types, handled missing values, and no duplicate records.

## 👨‍💻 Project

**Task:** Data Cleaning and Preprocessing
**Dataset:** Customer Personality Analysis
**Language:** Python
**Library:** Pandas
