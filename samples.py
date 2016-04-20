import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.DataFrame.from_csv('titanic_data.csv')
#
# titanic['Sex'].replace('female', 0, inplace=True)
# titanic['Sex'].replace('male', 1, inplace=True)
# titanic.fillna(value=0, inplace=True)
# mean = dict(titanic.groupby('Sex').mean()['Age'])
# print(mean)

a = 2
c = 3

a = 0 if a == c else a + 1

print(a)


class okC:

    def __init__(self):
        pass

    def run(self):
        po = 'po'
        return po

x = okC
y = x.run()
print(y)