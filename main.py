import pandas as pd

all_students = pd.read_csv("All Students.csv")
preference_responses = pd.read_csv("Preference Responses.csv")
program_data = pd.read_csv("Program Data.csv")
presenters = pd.read_csv("Presenters.csv")

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