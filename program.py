class Program:

    title = ''
    program_id = 0
    category = ''
    room = ''
    min_cap = 0
    max_cap = 0
    supervisor = ''
    students = []
    def __init__(self, title, program_id, category, room, min_cap, max_cap, supervisor):
        self.title = title
        self.program_id = program_id
        self.category = category
        self.room = room
        self.min_cap = min_cap
        self.max_cap = max_cap
        self.supervisor = supervisor
    
    def print_program(self):
        print(self.title, self.program_id, self.category, self.room, self.min_cap, self.max_cap, self.supervisor)