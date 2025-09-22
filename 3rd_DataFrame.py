import pandas as pd
import numpy as np

# DataFrame:

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
    }

print(data)

df = pd.DataFrame(data)
print(df)

df.head(2)
print(df.head(2))

df.tail(2)
print(df.tail(2))
 
# loc and iloc
# iloc

print(df.iloc[1:4, :2])  # rows, columns 

# loc

print(df.loc[1:3,["Age",'Department']])

print(df[["Age","Department"]])

print(df.drop("Age", axis = 1))

print(df.shape) # Rows #Column 

print(df.info())

print(df.describe())
