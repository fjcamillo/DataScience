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
#Cleaning
"""
2. Gender was Complete there was no null or nan value, created a proxy: male = 1, female = 0
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
titanic = pd.DataFrame.from_csv('titanic_data.csv')


def get_question_two(data):
    male_count = 0
    female_count = 0
    for i in range(1, len(data['Sex'])+1, 1):
        actual_values = list(data.loc[i:i, 'Sex'])
        survived = list(data.loc[i:i, 'Survived'])
        if str(actual_values[0]) == "male":
            data.loc[i:i, 'Sex'] = 1
            if survived[0] == 1:
                male_count += 1
        elif str(actual_values[0]) == "female":
            data.loc[i:i, 'Sex'] = 0
            if survived[0] == 1:
                female_count += 1
        else:
            pass

    # '#'Gets the total number of male that was on the ship
    number_of_male_ob = data['Sex'].sum()

    # '#'Gets the total number of female that was on the ship
    number_of_female_ob = data['Sex'].count() - int(number_of_male_ob)

    # '#'Get the total number of survivors from the data set
    total_number_of_survivors = data['Survived'].sum()

    return number_of_male_ob, number_of_female_ob, total_number_of_survivors, male_count, female_count


def main():
    question_two = get_question_two(titanic)
    print(question_two)

if __name__ == '__main__':
    main()
