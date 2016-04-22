import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')
#
# titanic['Sex'].replace('female', 0, inplace=True)
# titanic['Sex'].replace('male', 1, inplace=True)
# titanic.fillna(value=0, inplace=True)
# mean = dict(titanic.groupby('Sex').mean()['Age']
# print(mean)


a = 4
b = 2
a += 1 if a == 3 else b if a == 4 else a+3
print(a)

# lst = ['francisc', 'jerhone', 'camillo', 'francisc jerhone']
# x = [word for words in lst for word in words.split()]
# print(np.range(9))

