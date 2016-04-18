import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')

# print(titanic.loc())

# if titanic.values[0, 3] == "male":
#     print("Yey")

print(titanic.values[0])
# print(titanic.values[0, 3])
# print(titanic.columns)
# print(titanic)
# print(titanic.describe())
