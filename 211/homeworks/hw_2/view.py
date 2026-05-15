"""Homework 2
Quinn Smiley, 2026-04-13, CS 211"""


class View:
    def __init__(self): # Used Cursor to understand init structure
        pass

    def display_tasks(self, tasks):
        def completed(task): # Asked Cursor to help me structure completed() more efficiently
            return "yes" if task["completed"] else "no"

        if len(tasks) == 0:
            print("No tasks yet.")
            return

        for i in range(len(tasks)):
            task = tasks[i]
            print(f"{i + 1}. {task['description']} (completed? {completed(task)})")

    def show_menu(self):
        print("--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Mark Task as Incomplete")
        print("5. Remove Task")
        print("6. Exit")
        print("-----------------------")
        choice = input("Enter your choice (1-6): ")
        return choice
    
    def task_info(self, choice): 
        if choice == "1":
            return input("Task description: ")

        if choice in ("3", "4", "5"):
            raw = input("Enter task number: ")
            return int(raw) - 1

        return None
    
    def display_messages(self, key):
        messages = {
            "added" : "Task added successfully.", 
            "removed" : "Task removed successfully.", 
            "complete" : "Task marked complete.", 
            "incomplete" : "Task marked incomplete.", 
            "invalid_choice": "Invalid choice. Enter a number 1-6.",
            "marked_complete": "Task is already marked complete.", 
            "marked_incomplete" : "Task is already marked incomplete."
        }

        if key in messages:
            print(messages[key])
        else:
            print("Unknown message.")
    

if __name__ == "__main__":


    # Display Test
    v = View()
    # v.display_tasks([{"description": "Test", "completed": False}])

    # Show Menu Test
    # v.show_menu()

    # Task Info Test
    # v.task_info(4)

    # Messages Test
    # v.display_messages("complete")