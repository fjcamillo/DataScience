import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')

for i in range(1, len(titanic['Sex']), 1):
    if titanic['Sex'][i] == 'male':
        titanic['Sex'][i] = 1
    elif titanic['Sex'][i] == 'female':
        titanic['Sex'][i] = 0
    else:
        pass

print(titanic['Sex'])

dfmi.__getitem__('one').__setitem__('second', value)

# print(titanic.loc())

# if titanic.values[0, 3] == "male":
#     print("Yey")

# print(titanic['Sex'][1])
# print(titanic)
# print(titanic.values[0, 3])
# print(titanic.columns)
# print(titanic)
# print(titanic.describe())
