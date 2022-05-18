from importlib.metadata import distribution
import random
import pandas as pd
import copy

from program import Program
from student import Student
#reads all the files given
all_students = pd.read_csv("All Students.csv") # Emails of all the students
preference_responses = pd.read_csv("Responses.csv") # preferences of the students
program_data = pd.read_csv("Program Data.csv") # Data of each program and what happens
presenters = pd.read_csv("Presenters.csv") # emails of the presenters
student_choices = {} #creates a dictionary to store the student assignments

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
#all_students.to_csv("All Students.csv", index=False)

for column in preference_responses.columns:
    preference_responses['Email'] = preference_responses['Email'].str.lower()

#for column in presenters.columns:
#    presenters['Email'] = presenters['Email'].str.lower()

programs = []
for i in range(len(program_data)):
    program = Program(program_data["Program Title"][i],program_data['Program ID'][i],program_data["Category"][i],program_data["Room #"][i], program_data['Min Cap'][i],program_data['Max Cap'][i], program_data['Supervisor(s)'][i])
    programs.append(program)

students =[]
for i in range(len(all_students)):
    student = Student(all_students['Email'][i].lower(),all_students['Last_Name'][i], all_students['First_Name'][i])
    if student.email.lower() in presenters.values:
        student.presenter = True
    if student.email.lower() in preference_responses.values:
        row = preference_responses.index[preference_responses['Email'] == student.email][0]
        
        class1 = [preference_responses['What is your 1st choice session?'][row], preference_responses['What is your 2nd choice session?'][row], preference_responses['What is your 3rd choice session?'][row], preference_responses['What is your 4th choice session?'][row], preference_responses['What is your 5th choice session?'][row]]
        class2 = [preference_responses['What is your 1st choice session?.1'][row], preference_responses['What is your 2nd choice session?.1'][row], preference_responses['What is your 3rd choice session?.1'][row], preference_responses['What is your 4th choice session?.1'][row], preference_responses['What is your 5th choice session?.1'][row]]
        class3 = [preference_responses['What is your 1st choice session?.2'][row], preference_responses['What is your 2nd choice session?.2'][row], preference_responses['What is your 3rd choice session?.2'][row], preference_responses['What is your 4th choice session?.2'][row], preference_responses['What is your 5th choice session?.2'][row]]
        class4 = [preference_responses['What is your 1st choice session?.3'][row], preference_responses['What is your 2nd choice session?.3'][row], preference_responses['What is your 3rd choice session?.3'][row], preference_responses['What is your 4th choice session?.3'][row], preference_responses['What is your 5th choice session?.3'][row]]
        class5 = [preference_responses['What is your 1st choice session?.4'][row], preference_responses['What is your 2nd choice session?.4'][row], preference_responses['What is your 3rd choice session?.4'][row], preference_responses['What is your 4th choice session?.4'][row], preference_responses['What is your 5th choice session?.4'][row]]
        student.choices = [class1,class2,class3,class4,class5]
    students.append(student)

without_presenters = []
for s in students:
    if s.presenter == False:
        without_presenters.append(s)

students_no_pres = []
for s in students:
    if s.presenter == False:
        if len(s.choices) > 0:
            students_no_pres.append(s)

students_no_signup = []
for s in students:
    if s.presenter == False:
        if len(s.choices) == 0:
            students_no_signup.append(s)


# make a function to find the program based on the name
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


distributions = {}
for x in programs:
    if x.category == 1:
        distributions[x.program_id] = 0
for x in students_no_pres:
    if x.choices[0][0] in distributions:
        distributions[x.choices[0][0]] += 1


for x in distributions:
    if distributions[x] < find_program(x).min_cap:
        difference = find_program(x).min_cap - distributions[x]
        for y in range(difference):
            if len(students_no_signup) > 0:
                find_program(x).students.append(random.choice(students_no_signup))
                students_no_signup.remove(find_program(x).students[-1])
            else:
                break


for x in students_no_pres:
    print(x.email)

print()
print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
zy = 0
for person in students_no_pres: 
    print(person.email)
    first_choice = person.choices[0][0] # get the first choice of the student
    first_program = find_program(first_choice) # find the program that the student chose
    first_program.students.append(person) # add the student to the program
    person.which_choice = 0 # set the student's choice to 0 # remove the student from the list of students who didn't choose a presenter
    zy += 1

print(len(students_no_pres))
print(zy)


overflown_programs = []
for program in programs: # go through every program
    if program.is_available() == False: # if the program is oversubscribed
        overflown_programs.append(program) # add it to the list of overflown programs

num_of_people = 0
for x in programs:
    if x.category == 1:
        num_of_people += len(x.students) 


poor_kids = [] 
for oprogram in overflown_programs: # for every program that is oversubscribed
    while len(oprogram.students) > oprogram.max_cap: # if the program is oversubscribed, then we need to remove people from it
        poor_kids.append(random.choice(oprogram.students)) # randomly pick a student from the program
        oprogram.students.remove(poor_kids[-1]) # remove them from the program

for person in poor_kids:
    person.which_choice += 1 # add one to the student's choice 
    second_choice = person.choices[0][person.which_choice] # get the first choice of the student
    second_program = find_program(second_choice) # find the program that the student chose
    second_program.students.append(person) # add the student to the program




overflown_programs = []
for program in programs: # go through every program
    if program.is_available() == False: # if the program is oversubscribed
        overflown_programs.append(program) # add it to the list of overflown programs

poor_kids = [] 
for oprogram in overflown_programs: # for every program that is oversubscribed
    lol_kids = [] #kids in the program that have no choices so they go out first
    for x in oprogram.students:
        if len(x.choices) == 0:
            lol_kids.append(x)
            oprogram.students.remove(x)
    while len(oprogram.students) + len(lol_kids) > oprogram.max_cap: # if the program is oversubscribed, then we need to remove people from it
        if len(lol_kids) > 0:
            poor_kids.append(random.choice(lol_kids))
            lol_kids.remove(poor_kids[-1])
        else:
            poor_kids.append(random.choice(oprogram.students)) # randomly pick a student from the program
            oprogram.students.remove(poor_kids[-1]) # remove them from the program
    if len(lol_kids) > 0:
        for x in lol_kids:
            oprogram.students.append(x)

last_to_go = []
for person in poor_kids:
    if len(person.choices) == 0:
        last_to_go.append(person)
    else:    
        person.which_choice += 1 # add one to the student's choice 
        second_choice = person.choices[0][person.which_choice] # get the first choice of the student
        second_program = find_program(second_choice) # find the program that the student chose
        second_program.students.append(person) # add the student to the program

for x in last_to_go:
    for y in programs:
        if y.category == 1 and len(y.students) < y.max_cap:
            y.students.append(x)
            last_to_go.remove(x)
            break



for x in programs:
    if x.category == 1:
        print()
        print("program ID: ", x.program_id)
        print("number of students in program: ", len(x.students))
        # print the email of students attending the program
        for student in x.students:
            print(student.email)
        print()
