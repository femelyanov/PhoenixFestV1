class Student:

    timestamp = ""
    email = ""
    last_name = ""
    first_name = ""
    grade = ""
    choices = []
    assigned = [False,False,False,False]
    presenter = False

    def __init__(self, email, last_name, first_name):
        self.email = email
        self.last_name = last_name
        self.first_name = first_name

    def add_preference(self, class1_choices,class2_choices,class3_choices,class4_choices):
        self.choices = [class1_choices,class2_choices,class3_choices,class4_choices]