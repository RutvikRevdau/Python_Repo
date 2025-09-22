import pandas as pd
s = pd.Series([10,20,30,40,50,])
print(s)
print(s.dtype)
print(s.values)
print(s.index)
print(s.name)    # Default name is none 
s.name = 'calories'  # Rename of the column or the series 
print(s)
print(s.name)
print()
# Indexing (Normal Indexing )

print(s[0])
print()
print(s[0:2])  # Start(included) : stop (excluded) : step value (values to jump)

print(s[2:4])

# iloc -> location based indexing  (Indexing using iloc)

print(s.iloc[3])

print(s.iloc[[1,2,4]])

index = ["apple","banana","grapes","orange","strawberry"]

s.index = index   # To set different set of Indexing using s.index = index 
print(s)

print(s['grapes'])
print(s.iloc[3])

#loc -> label based indexing.
print(s.loc['grapes'])

# In label based indexing your start as well as stop value both are included in the output.
print(s['banana':'orange'])
