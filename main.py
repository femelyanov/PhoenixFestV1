import pandas as pd
import matplotlib.pyplot as plt
import pprint

from program import Program
from student import Student
cat1 = {} #key:presentation, value: names of people attending
students = {}
#reads all the files given
all_students = pd.read_csv("All Students.csv") # Emails of all the students
preference_responses = pd.read_csv("Preference Responses.csv") # preferences of the students
program_data = pd.read_csv("Program Data.csv") # Data of each program and what happens
presenters = pd.read_csv("Presenters.csv") # emails of the presenters
student_choices = {} #creates a dictionary to store the student assignments

#prints all the dataframes and their types
'''
print("All Students")
print(all_students.head())
print(all_students.dtypes)

print("\n Preference Responses")
print(preference_responses.head())
print(preference_responses.dtypes)

print("\n Program Data")
print(program_data.head())
print(program_data.dtypes)

print("\n Presenters")
print(presenters.head())
print(presenters.dtypes)
'''
pd.set_option('display.max_rows', None)
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
#all_students = all_students[~all_students['Email'].isin(presenters['Email'])]
#save all_students to a new csv file
#all_students.to_csv("All Students.csv", index=False)
#make all values in "Email" column in 'preference responses' lowercase
for column in preference_responses.columns:
    preference_responses['Email'] = preference_responses['Email'].str.lower()

for column in presenters.columns:
    presenters['Email'] = presenters['Email'].str.lower()

# Make a new file of just the people who have not chosen preferences
#delete all instances of values that are in 'preference_responses' from 'all_students'
#all_students = all_students[~all_students['Email'].isin(preference_responses['Email'])]
#save all_students to a new csv file
#all_students.to_csv("No Choices.csv", index=False)

#put the distribution of data for 'what is your 1st choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_1 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 1st choice session?'][i] in session_distribution_1_1:
        session_distribution_1_1[preference_responses['What is your 1st choice session?'][i]] += 1
    else:
        session_distribution_1_1[preference_responses['What is your 1st choice session?'][i]] = 1
#pprint.pprint(session_distribution_1_1)

#put the distribution of data for 'what is your 2nd choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_2 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 2nd choice session?'][i] in session_distribution_1_2:
        session_distribution_1_2[preference_responses['What is your 2nd choice session?'][i]] += 1
    else:
        session_distribution_1_2[preference_responses['What is your 2nd choice session?'][i]] = 1
#print(session_distribution_1_2)

#put the distribution of data for 'what is your 3rd choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_3 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 3rd choice session?'][i] in session_distribution_1_3:
        session_distribution_1_3[preference_responses['What is your 3rd choice session?'][i]] += 1
    else:
        session_distribution_1_3[preference_responses['What is your 3rd choice session?'][i]] = 1
#print(session_distribution_1_3)

#put the distribution of data for 'what is your 4th choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_4 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 4th choice session?'][i] in session_distribution_1_4:
        session_distribution_1_4[preference_responses['What is your 4th choice session?'][i]] += 1
    else:
        session_distribution_1_4[preference_responses['What is your 4th choice session?'][i]] = 1
#print(session_distribution_1_4)

#put the distribution of data for 'what is your 5th choice session?' in 'preference responses' into a dictionary
#key is the session name, value is the number of students in that session
session_distribution_1_5 = {}
for i in range(len(preference_responses)):
    if preference_responses['What is your 5th choice session?'][i] in session_distribution_1_5:
        session_distribution_1_5[preference_responses['What is your 5th choice session?'][i]] += 1
    else:
        session_distribution_1_5[preference_responses['What is your 5th choice session?'][i]] = 1
#print(session_distribution_1_5)
'''
# put the 'max cap' of each session into a dictionary
# key is the session name, value is the max cap of that session
max_cap = {}
for i in range(len(program_data)):
    max_cap[program_data['Program ID'][i]] = program_data['Max Cap'][i]
#pprint.pprint(max_cap)
def first_session ():
    session_1 = {}
    for x in session_distribution_1_1:
        if session_distribution_1_1[x] < max_cap[x]:
            session_1[x] = []
            for i in range(len(preference_responses)):
                if preference_responses['What is your 1st choice session?'][i] == x:
                    session_1[x].append(preference_responses['Email'][i])
    #pprint.pprint(capacity)
    pprint.pprint(session_1)

print("\n")

print(first_session())'''
programs = []
for i in range(len(program_data)):
    program = Program(program_data["Program Title"][i],program_data['Program ID'][i],program_data["Category"][i],program_data["Room #"][i], program_data['Min Cap'][i],program_data['Max Cap'][i], program_data['Supervisor(s)'][i])
    programs.append(program)

students =[]
for i in range(len(all_students)):
    #print(i)
    student = Student(all_students['Email'][i].lower(),all_students['Last'][i], all_students['First'][i])
    #print(student.email)
    if student.email.lower() in presenters.values:
        student.presenter = True
    if student.email.lower() in preference_responses.values:
        row = preference_responses.index[preference_responses['Email'] == student.email][0]
        
        class1 = [preference_responses['What is your 1st choice session?'][row], preference_responses['What is your 2nd choice session?'][row], preference_responses['What is your 3rd choice session?'][row], preference_responses['What is your 4th choice session?'][row], preference_responses['What is your 5th choice session?'][row]]
        class2 = [preference_responses['What is your 1st choice session?.1'][row], preference_responses['What is your 2nd choice session?.1'][row], preference_responses['What is your 3rd choice session?.1'][row], preference_responses['What is your 4th choice session?.1'][row], preference_responses['What is your 5th choice session?.1'][row]]
        class3 = [preference_responses['What is your 1st choice session?.2'][row], preference_responses['What is your 2nd choice session?.2'][row], preference_responses['What is your 3rd choice session?.2'][row], preference_responses['What is your 4th choice session?.2'][row], preference_responses['What is your 5th choice session?.2'][row]]
        class4 = [preference_responses['What is your 1st choice session?.3'][row], preference_responses['What is your 2nd choice session?.3'][row], preference_responses['What is your 3rd choice session?.3'][row], preference_responses['What is your 4th choice session?.3'][row], preference_responses['What is your 5th choice session?.3'][row]]
        student.choices = [class1, class2,class3,class4]

    students.append(student)
print(students)