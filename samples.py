import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')

for i in range(1, len(titanic['Sex']), 1):
    actual_values = list(titanic.loc[i:i, 'Sex'])
    if str(actual_values[0]) == "male":
        titanic.loc[i:i, 'Sex'] = 1

# print(titanic['Sex'])
# print(titanic.loc())
print(str(titanic.loc[12:12, 'Sex']))

# if titanic.values[0, 3] == "male":
#     print("Yey")

# print(titanic['Sex'][1])
# print(titanic)
# print(titanic.values[0, 3])
# print(titanic.columns)
# print(titanic)
# print(titanic.describe())
