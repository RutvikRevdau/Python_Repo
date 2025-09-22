import pandas as pd

csv_1 = pd.read_csv(r"C:\Python\Pandas\test.csv")
print(csv_1) 
print(csv_1.index)
print(csv_1.columns)
print(csv_1.describe())
print(csv_1.head(3))
print(csv_1.tail())
print(csv_1[:2])
print(csv_1[6:11])
print(type(csv_1))
print(csv_1.index.array)
csv_1.loc[0, "Region"] = "python"  # assignment
print(csv_1.loc[0, "Region"])      # print the updated value

print(csv_1)
print(csv_1.loc[[2,3],:])

print(csv_1.iloc[1,5])
print(csv_1.drop("Rep",axis=1))