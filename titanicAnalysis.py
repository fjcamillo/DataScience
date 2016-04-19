"""
This final project shall be composed of the analysis of the titanic data set
questions created:
1. What factors made people more likely to survive?
2. Does gender affect the survival of the on-board passengers and crew?
3. Does having a sibling or spouse on board affects the survival of the passenger?
4. Does economic status affects the survival of the person
5. Is there a relationship between the age and the location embarked from on the survival of the person?
6. Do persons with 2 or more first names have a higher chance of survival?
7. Does having a wife or husband (off board or on board) affect the chance of survival?
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
titanic = pd.DataFrame.from_csv('titanic_data.csv')


def get_question_one(data):
    pass


def get_question_two(data):

    # '#' Stores the number of living males
    male_count = 0

    # '#' Stores the number of living females
    female_count = 0

    # '#' Works on the data, changes male to 1, and female to 0
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

    total_count = data['Sex'].count()

    return number_of_male_ob, number_of_female_ob, total_number_of_survivors, male_count, female_count, total_count


def get_question_three(data):

    # '#' Stores the person with siblings count
    per_w_sibsp = 0

    # '#' Stores the surviving persons with siblings count
    survivors_w_sibsp = 0

    # '#' Works on the Data, counts the person with siblings and also counts
    # '#' the surviving persons that has a sibling on board
    for i in range(1, len(data['Sibsp'])+1, 1):
        test_sibsp = list(data.loc[i:i, "Sibsp"])
        survived = list(data.loc[i:i, "Survived"])
        if int(str(test_sibsp[0])) > 0:
            per_w_sibsp += 1
            if survived[0] == 1:
                survivors_w_sibsp += 1
        elif int(str(test_sibsp[0])) == 0:
            per_w_sibsp += 1
        else:
            pass

    # '#'Get the total number of survivors from the data set
    total_number_of_survivors = data['Survived'].sum()

    # '#'Gets the total number of siblings on board
    total_sibsps = data['Sibsp'].sum()

    return per_w_sibsp, survivors_w_sibsp, total_sibsps, total_number_of_survivors


def get_question_four(data):

    # '#' Stores the PClass data according to the economic status of the person
    thirdclass_total = 0
    secondclass_total = 0
    firstclass_total = 0

    # '#' Works on the Data, The PClass data is divided if the data is going to
    # '#' the third class, the second class, or the first class
    # '#' Also counts the number of persons that survived according to their economic status
    for i in range(1, len(data['Pclass']) + 1, 1):
        actual_class = list(data.loc[i:i, "Pclass"])
        survived = list(data.loc[i:i, "Survived"])
        if int(actual_class[0]) == 1:
            firstclass_total += 1
        elif int(actual_class[0]) == 2:
            secondclass_total += 1
        elif int(actual_class[0]) == 3:
            thirdclass_total += 1
        else:
            pass

    # '#'Get the total number of survivors from the data set
    total_number_of_survivors = data['Survived'].sum()

    return firstclass_total, secondclass_total, thirdclass_total, total_number_of_survivors


def get_question_five(data):
    froms = 0
    fromq = 0
    fromc = 0
    ageS = pd.DataFrame()
    ageC = pd.DataFrame()
    ageQ = pd.DataFrame()

    for i in range(1, len(data['Age'])+1, 1):
        location = list(data.loc[i:i, "Embarked"])
        actual_age = list(data.loc[i:i, "Age"])
        if str(location[0]).lower() == "s":
            froms += 1
            ageS.add(pd.DataFrame({
                str(actual_age[0]): 1
            }, index=['a']), fill_value=0)
        elif str(location[0]).lower() == "c":
            fromc += 1
            ageC.add(pd.DataFrame({
                str(actual_age[0]): 1
            }, index=['a']), fill_value=0)
        elif str(location[0]).lower() == "q":
            fromq += 1
            ageQ.add(pd.DataFrame({
                str(actual_age[0]): 1
            }, index=['a']), fill_value=0)
        else:
            pass

    total_number_of_survivors = data['Survived'].sum()

    summationS = ageS.sum(axis=0)
    summationQ = ageQ.sum(axis=0)
    summationC = ageC.sum(axis=0)

    return froms, fromq, fromc, total_number_of_survivors, summationC, summationQ, summationS


def get_question_six(data):
    name_guides = ['Mr.', 'Ms.', 'Miss.', 'Mister.', 'Mrs.', 'Don.',
                   'Master.', 'Rev.', 'Dr.', 'Mme.', 'Major.', 'Sir.',
                   'Miss', 'Ms', 'Mr', 'Rev', 'Mme', 'Master', 'Sir']
    two_firstname = 0
    one_firstname = 0
    morethantwo_firstname = 0
    for i in range(1, len(data['Survived'])+1, 1):
        actual_names = list(data.loc[i:i, "Name"])
        separated = str(actual_names[0]).split(" ")
        for j in range(0, len(separated), 1):
            if separated[j] in name_guides:
                firstname_count = len(separated) - (j+1)
                if firstname_count == 2:
                    two_firstname += 1
                elif firstname_count == 1:
                    one_firstname += 1
                elif firstname_count > 2:
                    morethantwo_firstname += 1

    return two_firstname, one_firstname, morethantwo_firstname


def get_question_seven(data):
    pass



def main():
    question_two = get_question_two(titanic)
    print("Question #2 Answer \n"
          "There are a total of %s persons on the data set \n"
          "There are %s Men and %s Women on board\n"
          "of the %s on-board only %s survived\n"
          "%s of those are men, while the remaining %s are women\n"
          % (question_two[5], question_two[0], question_two[1], question_two[5],
             question_two[2], question_two[3], question_two[4]))

    question_three = get_question_three(titanic)
    print("Question #3 Answer \n"
          "There are a total of %s persons on the data set\n"
          "The are %s persons on-board that had a sibling or a spouse with them\n"
          "%s persons with siblings survive the tragedy"
          % (question_three[3], question_three[0], question_three[1]))

    question_four = get_question_four(titanic)
    print(question_four, "Answers on question 4")

    question_five = get_question_five(titanic)
    print(question_five, "Answers on question 5")

    question_six = get_question_six(titanic)
    print(question_six, "Answers on question 6")

if __name__ == '__main__':
    main()
