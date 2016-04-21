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

def cleaner(data):
    data.fillna(value=0, inplace=True)

    # '#' Creates a dictionary that holds the mean for male and female
    mean = dict(titanic.groupby('Sex').mean()['Age'])

    # '#'Replaces the female with 0, male with 1
    data['Sex'].replace('female', 0, inplace=True)
    data['Sex'].replace('male', 1, inplace=True)

    # '#' Rounds the age using int() and converting fares to float
    for i in range(1, len(data['Age']), 1):
        d = int(float(list(data.loc[i:i, 'Age'])[0]))
        data.loc[i:i, 'Age'] = d
        f = float(list(data.loc[i:i, 'Fare'])[0])
        data.loc[i:i, 'Fare'] = f

    return data


def get_question_one(data):
    pass


def get_question_two(data):
    number_of_male_ob = data['Sex'].sum()
    number_of_female_ob = data['Sex'].count() - int(number_of_male_ob)
    total_number_of_survivors = data['Survived'].sum()
    total_count = data['Sex'].count()
    female_count = 0
    male_count = 0
    for i in range(1, len(data['Sex'])+1, 1):
        male_count += 1 if int(list(data.loc[i:i, 'Sex'])[0]) == 1 else 0
        female_count += 1 if int(list(data.loc[i:i, 'Sex'])[0]) == 0 else 0
    return number_of_male_ob, number_of_female_ob, total_number_of_survivors, male_count, female_count, total_count,


def get_question_three(data):
    per_w_sibsp = 0
    survivors_w_sibsp = 0

    # '#' Works on the Data, counts the person with siblings and also counts
    # '#' the surviving persons that has a sibling on board
    for i in range(1, len(data['Sibsp'])+1, 1):
        test_sibsp = list(data.loc[i:i, "Sibsp"])
        survived = list(data.loc[i:i, "Survived"])
        if int(str(test_sibsp[0])) > 0:
            per_w_sibsp += 1
            survivors_w_sibsp += 1 if survived[0] == 1 else 0

    total_number_of_survivors = data['Survived'].sum()
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
            x = pd.DataFrame({
                str(actual_age[0]): 1
            }, index=['summation'])
            ageS = ageS.add(x, fill_value=0)

        elif str(location[0]).lower() == "c":
            fromc += 1
            y = pd.DataFrame({
                str(actual_age[0]): 1
            }, index=['summation'])
            ageC = ageC.add(y, fill_value=0)
        elif str(location[0]).lower() == "q":
            fromq += 1
            z = pd.DataFrame({
                str(actual_age[0]): 1
            }, index=['summation'])
            ageQ = ageQ.add(z, fill_value=0)
        else:
            pass

    total_number_of_survivors = data['Survived'].sum()

    return froms, fromq, fromc, total_number_of_survivors, ageS, ageC, ageQ


def get_question_six(data):
    name_guides = ['Mr.', 'Ms.', 'Miss.', 'Mister.', 'Mrs.', 'Don.',
                   'Master.', 'Rev.', 'Dr.', 'Mme.', 'Major.', 'Sir.',
                   'Miss', 'Ms', 'Mr', 'Rev', 'Mme', 'Master', 'Sir']
    two_firstname = 0
    one_firstname = 0
    # checker = 0
    morethantwo_firstname = 0
    for i in range(1, len(data['Survived'])+1, 1):
        separated = str(list(data.loc[i:i, "Name"])[0]).split(" ")
        survival = int(list(data.loc[i:i, 'Survived'])[0])
        for j in range(0, len(separated)-1, 1):
            if separated[j] in name_guides and survival == 1:
                firstname_count = len(separated) - (j+1)
                if firstname_count == 2: two_firstname += 1
                elif firstname_count == 1: one_firstname += 1
                elif firstname_count > 2: morethantwo_firstname += 1

    return two_firstname, one_firstname, morethantwo_firstname,

def get_question_seven(data):
    survivor_sp = 0
    name_guides = ['Mrs.']
    for i in range(1, len(data['Survived']) + 1, 1):
        separated = str(list(data.loc[i:i, "Name"])[0]).split(" ")
        for j in range(0, len(separated) - 1, 1):
            if separated[j] in name_guides:
                if int(str(list(data.loc[i:i, 'Survived'])[0])) == 1:
                    survivor_sp += 1

    return str(survivor_sp)



def main():
    out = cleaner(titanic)

    question_one = get_question_one(out)
    # print(question_one)

    question_two = get_question_two(out)
    print("Question #2 Answer \n"
          "There are a total of %s persons on the data set \n"
          "There are %s Men and %s Women on board\n"
          "of the %s on-board only %s survived\n"
          "%s of those are men, while the remaining %s are women\n"
          % (question_two[5], question_two[0], question_two[1], question_two[5],
             question_two[2], question_two[3], question_two[4]))

    question_three = get_question_three(out)
    print("Question #3 Answer \n"
          "There are a total of %s persons on the data set\n"
          "The are %s persons on-board that had a sibling or a spouse with them\n"
          "%s persons with siblings survive the tragedy\n"
          % (question_three[0], question_three[3], question_three[1]))

    question_four = get_question_four(out)
    print("Question #4 Answer \n"
          "There are a total of %s persons on the data set\n"
          "%s are from the first class, %s are from the second class and %s are from the third class\n"
          % (question_four[3], question_four[0], question_four[1], question_four[2]))

    question_five = get_question_five(out)
    print("Question #5 Answer \n"
          "There are a total %s survivors on the data set\n"
          "%s are from S, %s are from Q, %s are from C.\n"
          "The ages will follow\n"
          % (question_five[3], question_five[0], question_five[1], question_five[2]))

    question_six = get_question_six(out)
    print("Question #6 Answer\n"
          "%s had 1 first name\n"
          "%s had 2 first names\n"
          "%s had more than 2 first names\n"
          % (question_six[1], question_six[0], question_six[2]))
    # print(question_six, "Answers on question 6\n")
#return two_firstname, one_firstname, morethantwo_firstname,

    question_seven = get_question_seven(out)
    print("Question #7 Answer\n"
          "%s Female that has husbands survived the tragedy"
          % (question_seven[0]))
    # print(questtion_seven, "Answers on Question 7\n")


def main_plot():

    # '#' Creates a bar graph for question # 2
    out = cleaner(titanic)
    # question2 = get_question_two(out)
    # bars = [question2[3], question2[4]]
    # plt.bar([1], bars[0], label='Male', width=0.35)
    # plt.bar([2], bars[1], label='Female', width =0.35)
    # plt.legend()
    # plt.xlabel('bar number')
    # plt.ylabel('bar height')
    # plt.title('Titanic Gender Analysis')
    # plt.show()

    # '#' Creates bar for question #2
    question2 = get_question_two(out)
    plt.subplot(221)
    plt.bar([1], question2[3], label='Male', width=0.35)
    plt.bar([2], question2[4], label='Female', width=0.35)
    plt.legend()
    plt.xLabel('bar number')
    plt.ylabel('bar height')
    plt.title('Titanic Gender Analysis')

    # '#' Creates bar for question #3
    question3 = get_question_three(out)
    plt.subplot(222)
    plt.bar()

    # '#' Creates bar for question #4
    question4 = get_question_four(out)

    # '#' Creates bar for question #5
    question5 = get_question_five(out)

    # '#' Creates bar for question #6
    question6 = get_question_six(out)

if __name__ == '__main__':
    main_plot()
