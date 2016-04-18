import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')

# print(titanic.loc())

print(titanic.values[0, 3])

# print(titanic.columns)
# print(titanic)
# print(titanic.describe())
