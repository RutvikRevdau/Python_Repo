import pandas as pd

fruit_protein = {
    "Avocado": 2.0,       # grams of protein
    "Guava": 2.6,
    "Blackberries": 2.0,
    "Oranges": 0.9,
    "Banana":1.1,
    "Apples": 0.3,
    "Kiwi": 1.1,
    "Pomegranate": 1.7,
    "Mango": 0.8,
    "Cherries": 1.0
}

print(type(fruit_protein))

s = pd.Series(fruit_protein, name = "Protien")
print(s)

# Conditional Selection:

print(s>1)
print(s[s>1])

# Logical Operators: and, or, not 

# And Operator
print([(s>0.5) & (s<2)])

print(s[(s>0.5) & (s<2)])

print(s[(s>0.5) & (s<=2)])

# Or Operator 

print([(s>0.5) | (s<2)])

print(s[(s>0.5) | (s<2)])

print(s[(s>0.5) | (s<=2)])

# Not Operator

print(s[~(s>1)])
 
 # Modifying the series 

s["Mango"] = 2.8
print(s)


