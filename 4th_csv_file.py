import pandas as pd

dis = {"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}

d = pd.DataFrame(dis)

print(d)

d.to_csv("Test_new.csv")
d.to_csv("Test_new1.csv",index=False)
d.to_csv("Test_new2.csv",index=False,header=[1,2,3])
d = pd.read_csv(r"C:\Python\Pandas\Test_new2.csv")

print("Our DataFrame......\n",d)

d = pd.read_csv(r"C:\Python\Pandas\Test_new2.csv",nrows=1)
print("First Row....\n",d)


d1 = pd.read_csv(r"C:\Python\Pandas\Test_new2.csv",usecols=["1","2"])
print("First Row....\n",d1)


d2 = pd.read_csv(r"C:\Python\Pandas\Test_new2.csv",index_col="1")
print("First Row....\n",d2)


d3 = pd.read_csv(r"C:\Python\Pandas\Test_new2.csv",header=2)
print("First Row....\n",d3)


d4 = pd.read_csv(r"C:\Python\Pandas\Test_new2.csv",names=["col1","col2","col3"])
print("First Row....\n",d4)


d1 = pd.read_csv(r"C:\Python\Pandas\Test_new2.csv",header=None, names=["asdf0","asdf1","asdf2"] )
print("First Row....\n",d1)


