import pandas as pd
from pandas.io.pytables import dropna_doc

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

#