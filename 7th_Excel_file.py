import pandas as pd

# Sample Data
data = {
    'Name': ['Rushabh', 'Rahul', 'Saurabh', 'Krushna', 'Gopal'],
    'Score': [85, 81, 92, 80, 95]
}

df = pd.DataFrame(data)

# Write to Excel
df.to_excel('students.xlsx', index=False, sheet_name='Scores', engine='openpyxl')  # Without Index Nos
df.to_excel('students1.xlsx', sheet_name='Scores', engine='openpyxl')              # With Index Nos

# Read an Excel File
df = pd.read_excel('students.xlsx', sheet_name='Scores', engine='openpyxl')
print(df)

# Filter Rows
high_scores = df[df['Score'] > 90]
print("High Scores:\n", high_scores)

# Add a new Column
df['Grade'] = ['A+', 'A', 'A', 'A+', 'O']

# Sort Values
sorted_df = df.sort_values(by='Score', ascending=False)
print("\nSorted by Score:\n", sorted_df)

# Group and Summarize
grouped_summary = df.groupby('Grade')[['Score']].mean()
print("\nGrouped by Grade:\n", grouped_summary)