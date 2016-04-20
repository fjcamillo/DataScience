import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')

a = ["sMrs"]

if "sMrs" in a:
    print("y")

# print(titanic.loc[1:1, "Embarked"])
# if titanic.values[0, 3] == "male":
#     print("Yey")

# print(titanic['Sex'][1])
# print(titanic)
# print(titanic.values[0, 3])
# print(titanic.columns)
# print(titanic)
# print(titanic.describe())
