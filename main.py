import pandas as pd
from pandas.io.pytables import dropna_doc

all_students = pd.read_csv("All Students.csv")
preference_responses = pd.read_csv("Preference Responses.csv")
program_data = pd.read_csv("Program Data.csv")
presenters = pd.read_csv("Presenters.csv")
student_choices = {}
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
pd.set_option('display.max_rows', None)
pr = preference_responses.sort_values(by=['What grade are you in?'])
pr.to_csv("Preference Responses.csv", index=False)

#make all values in column lowercase
for column in all_students.columns:
    all_students['Email'] = all_students['Email'].str.lower()
#make all vlaues in 'Email' column in presenters lowercase
for column in presenters.columns:
    presenters['Email'] = presenters['Email'].str.lower()
#delete all instances of values that are in 'presenters' from 'all_students'
all_students = all_students[~all_students['Email'].isin(presenters['Email'])]
#save all_students to a new csv file
all_students.to_csv("All Students.csv", index=False)
#check if values of 'Email' column in 'all_students' are in 'presenters'
print(all_students['Email'].isin(presenters['Email']))
