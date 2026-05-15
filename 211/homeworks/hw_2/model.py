"""Homework 2
Quinn Smiley, 2026-04-13, CS 211"""

class Task: 

    def __init__(self, description, completed = False):
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}
    
    @staticmethod # Asked Cursor which would be best, @staticmethod or @classmethod
    def from_dict(data):
        return Task(data["description"], data["completed"]) # Asked Cursor how to extract information from a task in order to align with the parameters in __init__
    
    def __repr__(self):
        return f"{self.description}"

    

class Model: 
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append({'description': description, 'completed': False})
    
    def remove_task(self, index):
        self.tasks.remove(self.tasks[index])
    
    def all_tasks(self):
        return self.tasks
    
    def toggle_task(self, index):
        self.tasks[index]['completed'] = not self.tasks[index]["completed"]
    
    
    
    

if __name__ == "__main__":
    # Model Tests

    task_1 = Task('Buy groceries', False)
    task_2 = Task('Eat Lunch', False)
    
    # Add Test
    m = Model()
    m.add_task(task_1)
    m.add_task(task_2)
    # print(repr(m.tasks))

    # Remove Test
    # m.remove_task(0)
    # print(repr(m.tasks))

    # All Test
    test_all = m.all_tasks()
    # print(repr(test_all))

    # Toggle Test
    # print("Before:", m.all_tasks()) # Asked Cursor the best way to test the toggle method
    # m.toggle_task(0)
    # print("After:", m.all_tasks())

