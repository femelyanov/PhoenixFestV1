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

students_no_pres = []
for s in students:
    if s.choices and s.presenter == False:
        students_no_pres.append(s)

def find_program(id):
    for p in programs:
        if p.program_id == id:
            return p

    return None

def find_student(email):
    for s in students:
        if s.email == email:
            return s

    return None

def is_program_full(program):
    if program.max_cap == len(program.students):
        return True

def are_programs_full():
    for p in programs:
        if is_program_full(p):
            return True

    return False

'''extra_students = []
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
#print("Need people: ", all_diff)'''

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


# Give everybody their first-choice courses.  If any are oversubscribed, 
# then randomly pick a subset to get in and assign those people 
# their second-choice course, repeating as necessary.
for x in students:
    pass
    #print(x.choices)

for person in students_no_pres: 
    first_choice = person.choices[0][0] # get the first choice of the student
    first_program = find_program(first_choice) # find the program that the student chose
    first_program.students.append(person) # add the student to the program

overflown_programs = []
for program in programs: # go through every program
    if program.is_available() == False: # if the program is oversubscribed
        overflown_programs.append(program) # add it to the list of overflown programs

poor_kids = [] 
for oprogram in overflown_programs: # for every program that is oversubscribed
    while len(oprogram.students) > oprogram.max_cap: # if the program is oversubscribed, then we need to remove people from it
        poor_kids.append(random.choice(oprogram.students)) # randomly pick a student from the program
        oprogram.students.remove(poor_kids[-1]) # remove them from the program

for person in poor_kids: 
    second_choice = person.choices[0][1] # get the first choice of the student
    second_program = find_program(second_choice) # find the program that the student chose
    second_program.students.append(person) # add the student to the program

overflown_programs = []
for program in programs: # go through every program
    if program.is_available() == False: # if the program is oversubscribed
        overflown_programs.append(program) # add it to the list of overflown programs



for x in programs:
    print()
    print("program ID: ", x.program_id)
    print()
    print(x.students)
    print()
    print("number of students in program: ", len(x.students))
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~")

