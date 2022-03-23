import pandas as pd
import matplotlib.pyplot as plt
import pprint
from hungarian_algorithm import algorithm
import random

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
'''
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

def find_program(id):
    for p in programs:
        if p.program_id == id:
            return p

    return None

for i in programs:
    print(i.program_id, len(i.students)) # print each program and how many students are in the program

extra_students = []
no_left = 0
for student in students: # goes through every student
    if student.presenter == True: #if presenter, pass
        #print(student.email, "is presenter")
        pass
    elif len(student.choices) == 0: # if didnt make choices, then put him in the 'extra students' container
        extra_students.append(student)
    else:
        print(student.choices[0]) # print the choices of the student
        for pr_id in student.choices[0]: # for every program id, go through every choice that the student has
            program = find_program(pr_id)
            if program.is_available(): # checks if a program is available
                program.students.append(student.email) # append the email to the list of students attending the program
                student.assigned[0] = True # change the status of the student
                break
        if student.assigned[0] == False: # if none of the 5 choices are available, put the student into the 'extra students' container
            extra_students.append(student)
    no_left += 1
#print("no left: ", no_left)
all_diff = 0
for p in range(0,21): # go through every program (put 0-21) because there are 21 programs in the first category
    program = programs[p]
    difference = 0
    if len(program.students) < program.min_cap:
        difference = program.min_cap - len(program.students) # difference between the minimum cap and the number of students in there (so we can see how many students need to be added to satisfy the min cap)
        all_diff += difference # see how many people we need
#print("Need people: ", all_diff)

y = 0
z = 0
o = 0
for x in students: # get the distribution of presenters, 
    if x.presenter == True:
        y+=1
    if len(x.choices) == 0:
        z+=1
    #print(x.choices)
    if x.presenter == True and len(x.choices) > 0:
        o += 1
#print("presenters: ",y)
#print("no choices: ",z)
#print("presenter with choices: ",o)
#print(len(extra_students))

#print(len(students))
#for i in programs:
#    print(i.program_id, len(i.students))

test_list = []
distribution = {}
for student in students: # prints the dictionary of distribution of the choices 
    if student.presenter == True:
        #print(student.email, "is presenter")
        pass
    elif len(student.choices) == 0:
        test_list.append(student)
    else:
        for choice in student.choices[0]:
            if choice in distribution:
                distribution[choice] += 1
            else:
                distribution[choice] = 1
print(distribution)
'''
extra_students_test = []
for student in students:
    if student.presenter == True:
        #print(student.email, "is presenter")
        pass
    elif len(student.choices) == 0:
        extra_students_test.append(student)
    else:
        final_id = 0
        cap = 999
        for choice in student.choices[0]:
            prog_capa = len(find_program(choice).students)
            if find_program(choice).is_available() == True:
                if prog_capa < cap:
                    cap = prog_capa
                    final_id = choice
            find_program(final_id).students.append(student.email)
        #print(student.email, "final ID: ", final_id)
        if student.assigned[0] == False:
            extra_students.append(student)

#for i in programs:
#    print(i.program_id, len(i.students))
'''

