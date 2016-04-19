"""
This final project shall be composed of the analysis of the titanic data set
questions created:
1. What factors made people more likely to survive?
2. Does gender affect the survival of the on-board passengers and crew?
3. Does having a sibling or spouse on board affects the survival of the passenger?
4. Does economic status affects the survival of the person
5. Is there a relationship between the age and the location embarked from on the  survival of the person?
6. Do persons with 2 or more first names have a higher chance of survival?
7. Does having a wife or husband (off board or on board) affect the chance of survival?
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
# style('ggplot')
titanic = pd.DataFrame.from_csv('titanic_data.csv')


def getQuestionTwo(data):
    for i in range(1, len(data['Sex'])+1, 1):
        actual_values = list(data.loc[i:i, 'Sex'])
        if str(actual_values[0]) == "male":
            data.loc[i:i, 'Sex'] = 1
        elif str(actual_values[0]) == "female":
            data.loc[i:i, 'Sex'] = 0
        else:
            pass
    return data['Sex']


def main():
    question_two = getQuestionTwo(titanic)
    print(question_two)

if __name__ == '__main__':
    main()