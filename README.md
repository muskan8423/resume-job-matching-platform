# Resume Job Matching Platform

A Python-based Resume Job Matching Platform that aims to match candidates with suitable job roles based on their skills, experience, education, and resume information.

## Week 1 - Pandas Basics and Data Cleaning

### Objective

The objective of Week 1 is to learn Pandas basics and understand how to load, explore, and clean resume data.

### Topics Covered

- Pandas basics
- DataFrames
- Loading CSV files
- Exploring datasets
- Features and labels
- Missing values
- Duplicate records
- Data cleaning
- Saving cleaned data

## Features and Labels

### Features

Features are the input values used by the system.

For this project, the features are:

- Skills
- Experience
- Education

### Label

A label is the target or output value.

For this project:

`Job_Role`

is considered the label.

## Dataset

The sample dataset contains:

| Column | Description |
|---|---|
| Name | Candidate name |
| Skills | Candidate's skills |
| Experience | Years of experience |
| Education | Educational qualification |
| Job_Role | Job role |

## Data Cleaning

The following operations were performed:

1. Loaded the CSV dataset using Pandas.
2. Displayed the first rows of the dataset.
3. Checked the dataset shape.
4. Checked column names.
5. Checked data types.
6. Checked missing values.
7. Checked duplicate records.
8. Removed duplicate records.
9. Filled missing values.
10. Saved the cleaned dataset.

## Project Structure

```text
resume-job-matching-platform/
│
├── README.md
│
└── Week1/
    ├── sample_dataset.csv
    ├── pandas_basic.py
    ├── cleaned_dataset.csv
    └── week1_notes.md# resume-job-matching-platform
A Python-based Resume Job Matching Platform using Pandas for dataset loading, cleaning, feature preparation, and job-resume matching.
