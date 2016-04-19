import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')

sample_df = pd.DataFrame({
    'a': [1,2,3,4,5,6,7],
    'b': [9,8,7,4,5,6,3]
}, index=['q','w','e','r','t','y','u'])

print(sample_df)
# if titanic.values[0, 3] == "male":
#     print("Yey")

# print(titanic['Sex'][1])
# print(titanic)
# print(titanic.values[0, 3])
# print(titanic.columns)
# print(titanic)
# print(titanic.describe())
