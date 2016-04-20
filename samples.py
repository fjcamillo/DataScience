import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')

titanic['Sex'].replace('female', 0, inplace=True)
titanic['Sex'].replace('male', 1, inplace=True)
titanic.fillna(value=0, inplace=True)
mean = titanic.groupby('Sex').mean()['Age']
print(mean)