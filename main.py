from tkinter import N
import pandas as pd
import matplotlib.pyplot as plt
import pprint
from hungarian_algorithm import algorithm
import random
import collections

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
        #print(student.choices[0]) # print the choices of the student
        pass
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
            #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #print(student.choices[0])
            if choice in distribution:
                distribution[choice] += 1
            else:
                distribution[choice] = 1

ordered_distribution = collections.OrderedDict(sorted(distribution.items()))
print()
print(distribution)
print()
print(ordered_distribution)
'''
not_enough_people = []
for key in distribution:
    for period in programs:
        if period.program_id == key:
            if distribution[key] < period.min_cap:
                #print("not enough people")
                not_enough_people.append(period.program_id)

for i in programs:
    if i in not_enough_people:
        for person in students:
            if i.program_id in person.choices[0]:
                i.students.append(person.email)

for i in programs:
    if i in not_enough_people:
        if len
'''
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

# Give everybody their first-choice courses.  If any are oversubscribed, 
# then randomly pick a subset to get in and assign those people 
# their second-choice course, repeating as necessary.

for person in students:
    person.choices[0][0]

    '''
    Get distribution of all the choices (1-5)
If there are fewer sign-ups than the minimum, put all of the people that signed up for that class, into it
Because we know that even with those students the minimum number would not be met, fill the rest of the positions with people that did not sign up until the minimum number required
Then, we go through every person and give them their first choice if available, and if not, their second choice, and so on and if none of them are available, we throw them into the “extra” pile for now
After everyone is done, we check 

    '''