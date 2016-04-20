import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')

a = pd.DataFrame({'b':1}, index=['sum'])

b = pd.DataFrame({'a':2}, index=['sum'])

c = a.add(b, fill_value=0)

print(c)

# print(titanic.loc[1:1, "Embarked"])
# if titanic.values[0, 3] == "male":
#     print("Yey")

# print(titanic['Sex'][1])
# print(titanic)
# print(titanic.values[0, 3])
# print(titanic.columns)
# print(titanic)
# print(titanic.describe())
