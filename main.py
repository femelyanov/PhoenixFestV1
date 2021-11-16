import pandas as pd
import matplotlib.pyplot as plt

#reads all the files given
all_students = pd.read_csv("All Students.csv")
preference_responses = pd.read_csv("Preference Responses.csv")
program_data = pd.read_csv("Program Data.csv")
presenters = pd.read_csv("Presenters.csv")
student_choices = {} #creates a dictionary to store the student assignments

#prints all the dataframes and their types
'''
print("All Students")
print(all_students.head())
print(all_students.dtypes)

print("\n \n Preference Responses")
print(preference_responses.head())
print(preference_responses.dtypes)

print("\n \n Program Data")
print(program_data.head())
print(program_data.dtypes)

print("\n \n Presenters")
print(presenters.head())
print(presenters.dtypes)
'''

#sorts the preference responses by grade level (9->12) and saves (to the same file)
pr = preference_responses.sort_values(by=['What grade are you in?'])
pr.to_csv("Preference Responses.csv", index=False)

#formats the data and gets the final list of just the students that did not sign up
#make all values in 'Email'column in all_students lowercase
for column in all_students.columns:
    all_students['Email'] = all_students['Email'].str.lower()
#make all vlaues in 'Email' column in presenters lowercase
for column in presenters.columns:
    presenters['Email'] = presenters['Email'].str.lower()
#delete all instances of values that are in 'presenters' from 'all_students'
all_students = all_students[~all_students['Email'].isin(presenters['Email'])]
#save all_students to a new csv file
all_students.to_csv("All Students.csv", index=False)
#make all values in "Email" column in 'preference responses' lowercase
for column in preference_responses.columns:
    preference_responses['Email'] = preference_responses['Email'].str.lower()
#delete all instances of values that are in 'preference_responses' from 'all_students'
all_students = all_students[~all_students['Email'].isin(preference_responses['Email'])]
#save all_students to a new csv file
all_students.to_csv("All Students1.csv", index=False)

#put the distribution of data for 'what is your 1st choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_1 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 1st choice session?'][i] in session_distribution_1_1:
        session_distribution_1_1[preference_responses['What is your 1st choice session?'][i]] += 1
    else:
        session_distribution_1_1[preference_responses['What is your 1st choice session?'][i]] = 1
print(session_distribution_1_1)

#put the distribution of data for 'what is your 2nd choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_2 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 2nd choice session?'][i] in session_distribution_1_2:
        session_distribution_1_2[preference_responses['What is your 2nd choice session?'][i]] += 1
    else:
        session_distribution_1_2[preference_responses['What is your 2nd choice session?'][i]] = 1
print(session_distribution_1_2)

#put the distribution of data for 'what is your 3rd choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_3 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 3rd choice session?'][i] in session_distribution_1_3:
        session_distribution_1_3[preference_responses['What is your 3rd choice session?'][i]] += 1
    else:
        session_distribution_1_3[preference_responses['What is your 3rd choice session?'][i]] = 1
print(session_distribution_1_3)

#put the distribution of data for 'what is your 4th choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_4 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 4th choice session?'][i] in session_distribution_1_4:
        session_distribution_1_4[preference_responses['What is your 4th choice session?'][i]] += 1
    else:
        session_distribution_1_4[preference_responses['What is your 4th choice session?'][i]] = 1
print(session_distribution_1_4)

#put the distribution of data for 'what is your 5th choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_5 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 5th choice session?'][i] in session_distribution_1_5:
        session_distribution_1_5[preference_responses['What is your 5th choice session?'][i]] += 1
    else:
        session_distribution_1_5[preference_responses['What is your 5th choice session?'][i]] = 1
print(session_distribution_1_5)

