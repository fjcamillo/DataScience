"""
This final project shall be composed of the analysis of the titanic data set
questions created:
1. What factors made people more likely to survive? --Given by the site
2. Does gender affect the survival of the on-board passengers and crew?
3. Does having a sibling or spouse on board affects the survival of the passenger?
4. Does economic status affects the survival of the person
5. Is there a relationship between the age and the location embarked from on the survival of the person?
6. Do persons with 2 or more first names have a higher chance of survival?
7. Does having a wife or husband (off board or on board) affect the chance of survival?
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# '#' Titanic_data.csv to Pandas Data Frame
titanic = pd.DataFrame.from_csv('titanic_data.csv')

# '#' Takes in the titanic dataframe then cleans it
def cleaner(data):
    data.fillna(value=0, inplace=True)

    # '#' female are changed to 0, male are changed to 1
    data['Sex'].replace('female', 0, inplace=True)
    data['Sex'].replace('male', 1, inplace=True)

    # '#' Converts all floats and ints to their correct data type
    for i in range(1, len(data['Age']), 1):
        d = int(float(list(data.loc[i:i, 'Age'])[0]))
        data.loc[i:i, 'Age'] = d
        f = float(list(data.loc[i:i, 'Fare'])[0])
        data.loc[i:i, 'Fare'] = f

    return data

# '#' Answers Question #2
# '#' Adds all the male and female that survived
def get_question_two(data):

    # '#' Sums up all 1 on the 'Sex' Column
    number_of_male_ob = data['Sex'].sum()

    # '#' Subtracts the total count to the number_of_male_ob
    number_of_female_ob = data['Sex'].count() - int(number_of_male_ob)

    # '#' Sums up all 1 on the 'Survivor' Column
    total_number_of_survivors = data['Survived'].sum()
    total_count = data['Sex'].count()
    female_count = 0
    male_count = 0

    # '#' Counts the male survivor and the female survivor
    for i in range(1, len(data['Sex'])+1, 1):
        male_count += 1 if int(str(list(data.loc[i:i, 'Sex'])[0])) == 1 and int(
            str(list(data.loc[i:i, 'Survived'])[0])) == 1 else 0
        female_count += 1 if int(str(list(data.loc[i:i, 'Sex'])[0])) == 0 and int(
            str(list(data.loc[i:i, 'Survived'])[0])) == 1 else 0

    return number_of_male_ob, number_of_female_ob, total_number_of_survivors, male_count, female_count, total_count,


# '#' Answers Question #3
def get_question_three(data):
    per_w_sibsp = 0
    survivors_w_sibsp = 0

    # '#' Counts the persons that survives that has their siblings or spouse with them
    for i in range(1, len(data['Sibsp'])+1, 1):
        test_sibsp = list(data.loc[i:i, "Sibsp"])
        survived = list(data.loc[i:i, "Survived"])
        if int(str(test_sibsp[0])) > 0:
            per_w_sibsp += 1
            survivors_w_sibsp += 1 if survived[0] == 1 else 0

    total_number_of_survivors = data['Survived'].sum()
    total_sibsps = data['Sibsp'].sum()

    return per_w_sibsp, survivors_w_sibsp, total_sibsps, total_number_of_survivors


# '#' Answers Question #4
# '#' in each status
def get_question_four(data):
    thirdclass_total = 0
    secondclass_total = 0
    firstclass_total = 0
    survived_first = 0
    survived_second = 0
    survived_third = 0

    # '#' Classifies all of the survivors according to their economic status then counts how many survives
    for i in range(1, len(data['Pclass']) + 1, 1):

        # '#' stores a singe itemed list to actual_class
        actual_class = list(data.loc[i:i, "Pclass"])
        if int(actual_class[0]) == 1:
            firstclass_total += 1

            # '#' if the current person survive(get data from 'Survived column', add a 1 to survived_first
            survived_first += 1 if int(str(list(data.loc[i:i, 'Survived'])[0])) == 1 else 0
        elif int(actual_class[0]) == 2:
            secondclass_total += 1
            survived_second += 1 if int(str(list(data.loc[i:i, 'Survived'])[0])) == 1 else 0
        elif int(actual_class[0]) == 3:
            thirdclass_total += 1
            survived_third += 1 if int(str(list(data.loc[i:i, 'Survived'])[0])) == 1 else 0

    total_number_of_survivors = data['Survived'].sum()

    return firstclass_total, secondclass_total, thirdclass_total, total_number_of_survivors, survived_first, survived_second, survived_third


# '#' Answers Question #5


def get_question_five(data):
    froms = 0
    fromq = 0
    fromc = 0
    ageS = pd.DataFrame()
    ageC = pd.DataFrame()
    ageQ = pd.DataFrame()
    survivedS = 0
    survivedC = 0
    survivedQ = 0

    # '#' Counts the number of person that came from S, Q, C and then counts the number of survivors from each location
    # '#' Then counts the ages of the person on each location --> Not included on the final graph
    for i in range(1, len(data['Age'])+1, 1):
        location = list(data.loc[i:i, "Embarked"])
        actual_age = list(data.loc[i:i, "Age"])
        if str(location[0]).lower() == "s":
            froms += 1
            x = pd.DataFrame({str(actual_age[0]): 1}, index=['summation'])
            ageS = ageS.add(x, fill_value=0)
            survivedS += 1 if int(str(list(data.loc[i:i, 'Survived'])[0])) == 1 else 0
        elif str(location[0]).lower() == "c":
            fromc += 1
            y = pd.DataFrame({str(actual_age[0]): 1}, index=['summation'])
            ageC = ageC.add(y, fill_value=0)
            survivedC += 1 if int(str(list(data.loc[i:i, 'Survived'])[0])) == 1 else 0
        elif str(location[0]).lower() == "q":
            fromq += 1
            z = pd.DataFrame({str(actual_age[0]): 1}, index=['summation'])
            ageQ = ageQ.add(z, fill_value=0)
            survivedQ += 1 if int(str(list(data.loc[i:i, 'Survived'])[0])) == 1 else 0
        else:
            pass

    total_number_of_survivors = data['Survived'].sum()
    return froms, fromq, fromc, total_number_of_survivors, ageS, ageC, ageQ, survivedS, survivedQ, survivedC


# '#' Answers Question #6
def get_question_six(data):
    name_guides = ['Mr.', 'Ms.', 'Miss.', 'Mister.', 'Mrs.', 'Don.',
                   'Master.', 'Rev.', 'Dr.', 'Mme.', 'Major.', 'Sir.',
                   'Miss', 'Ms', 'Mr', 'Rev', 'Mme', 'Master', 'Sir']
    two_firstname = 0
    one_firstname = 0
    morethantwo_firstname = 0

    # '#' Counts the number of persons with 1 first name, 2 first names, and more than 2 first names
    for i in range(1, len(data['Survived'])+1, 1):
        separated = str(list(data.loc[i:i, "Name"])[0]).split(" ")
        survival = int(list(data.loc[i:i, 'Survived'])[0])
        for j in range(0, len(separated)-1, 1):
            if separated[j] in name_guides and survival == 1:
                firstname_count = len(separated) - (j+1)
                two_firstname += 1 if firstname_count == 2 else 0
                one_firstname += 1 if firstname_count == 1 else 0
                morethantwo_firstname += 1 if firstname_count > 2 else 0

    return two_firstname, one_firstname, morethantwo_firstname


# '#' Answers Question #7
def get_question_seven(data):
    survivor_sp = 0
    married = 0
    withthem = 0
    name_guides = ['Mrs.', 'Mrs', "Mrs.", 'mrs.', 'mrs']

    # '#' Counts the number of married females on the ship then classfies it they survives
    # '#' Also took into account if the females husband is on the ship as well
    for i in range(1, data['Survived'].count()+1, 1):
        separated = str(list(data.loc[i:i, "Name"])[0]).split(" ")
        for j in range(0, len(separated) - 1, 1):
            if separated[j] in name_guides:
                married += 1
                if int(str(list(data.loc[i:i, 'Survived'])[0])) == 1:
                    survivor_sp += 1
                    withthem += 1 if int(str(list(data.loc[i:i, 'Sibsp'])[0])) > 0 else 0

    output = survivor_sp
    return output, married, withthem


# '#' Plots
def main_plot():
    out = cleaner(titanic)
    question2 = get_question_two(out)
    plt.subplot(231)
    plt.autoscale(True)
    labelMe = ['Male', 'Male Survivor', 'Female', 'Female Survivor']
    points = [0, 3, 1, 4]
    for i in range(0, len(labelMe), 1):
        plt.bar([i+1], question2[points[i]], label=str(labelMe[i]),
                width=0.5, color=('#1C6972' if i % 2 != 0 else 'grey'))
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('bar number')
    plt.ylabel('bar height')
    plt.xlim(0, 5)
    plt.title('Titanic Gender Analysis')

    # '#' Creates bar for question #3
    question3 = get_question_three(out)
    plt.subplot(232)
    plt.autoscale(True)
    plt.bar([1], question3[0], label='With Sibsp', width=0.35, color='#0072BF')
    plt.bar([2], question3[1], label='Survivors-w-Sibsp', width=0.35, color='#004473')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('bar number')
    plt.ylabel('bar height')
    plt.xlim(0, 4)
    plt.title('Titanic Sibling Analysis')

    # '#' Creates pie for question #4
    question4 = get_question_four(out)
    plt.subplot(233)
    plt.autoscale(True)
    plt.pie(question4[4:7], labels=['1st-C', '2nd-C', '3rd-C'], colors=['#2BA4B2', '#1C6972', '#3BDEF2'],
            shadow=True, autopct='%1.1f%%')
    plt.title('Titanic Economic Status Analysis')

    # '#' Creates bar for question #5
    question5 = get_question_five(out)
    plt.subplot(234)
    plt.autoscale(True)
    fromCountry = ['From S', 'S Survivors', 'From C', 'C Survivors', 'From Q', 'Q Survivors']
    nums = [0, 7, 1, 8, 2, 9]
    for i in range(0, len(fromCountry), 1):
        plt.bar([i+1], question5[nums[i]], label=str(fromCountry[i]),
                width=0.35, color=('#426BBF' if i % 2 != 0 else 'grey'))
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('bar number')
    plt.ylabel('bar height')
    plt.xlim(0, 8)
    plt.title('Titanic Embarked Analysis')

    # '#' Creates bar for question #6
    question6 = get_question_six(out)
    plt.subplot(235)
    plt.autoscale(True)
    plt.bar([1], question6[1], label="One 1st Name", width=0.35, color='#426BBF')
    plt.bar([2], question6[0], label="Two 1st Name", width=0.35, color='#0072BF')
    plt.bar([3], question6[2], label=">2 1st Name", width=0.35, color='#004473')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('bar number')
    plt.ylabel('bar height')
    plt.xlim(0, 5)
    plt.title('Titanic first name analysis')

    # '#' Creates a bar for question #7
    question7 = get_question_seven(out)
    plt.subplot(236)
    plt.autoscale(True)
    plt.bar([1], question7[1], label="Total", width=0.35, color='#426BBF')
    plt.bar([2], question7[0], label="Survivor", width=0.35, color='#0072BF')
    plt.bar([3], question7[2], label="Spouse OB", width=0.35, color='#004473')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('bar number')
    plt.ylabel('bar height')
    plt.xlim(0, 5)
    plt.title('Titanic Married Analysis')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main_plot()
