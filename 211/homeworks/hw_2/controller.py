"""Homework 2
Quinn Smiley, 2026-04-13, CS 211"""

from model import Model
from view import View

class Controller: 
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        
    def main_loop(self): # Asked Cursor to help me make sure my logic was efficient and accurate
        while True: 
            choice = self.view.show_menu()

            if choice == "6": 
                break

            info = self.view.task_info(choice)

            if choice == "1": 
                self.model.add_task(info)
                self.view.display_messages("added")

            elif choice == "2": 
                tasks = self.model.all_tasks()
                self.view.display_tasks(tasks)

            elif choice == "3": 
                tasks = self.model.all_tasks()
                index = info
                if tasks[index]["completed"] == False:
                    self.model.toggle_task(index)
                    self.view.display_messages("complete")
                else: 
                    self.view.display_messages("marked_complete")

            elif choice == "4": 
                tasks = self.model.all_tasks()
                index = info
                if tasks[index]["completed"] == True:
                    self.model.toggle_task(index)
                    self.view.display_messages("incomplete")
                else: 
                    self.view.display_messages("marked_incomplete")

            elif choice == "5": 
                self.model.remove_task(info)
                self.view.display_messages("removed")

            else: 
                self.view.display_messages("invalid_choice")

    def menu(self):
        self.main_loop()

    

if __name__ == "__main__":
    m = Model()
    m.add_task("Buy groceries")
    m.add_task("Eat Lunch")

    v = View()

    c = Controller(m, v)
    c.main_loop()