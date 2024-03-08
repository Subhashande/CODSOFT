import os
import pickle
class TodoList:
    def __init__(self):
        self.tasks = []
        self.file_path = 'todo_list.pkl'
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as f:
                self.tasks = pickle.load(f)
    def save_tasks(self):
        with open(self.file_path, 'wb') as f:
            pickle.dump(self.tasks, f)
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")
        self.save_tasks()
    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            completed_task = self.tasks.pop(index - 1)
            print(f"Task '{completed_task}' marked as completed.")
            self.save_tasks()
        else:
            print("Invalid task index.")
    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task '{deleted_task}' deleted from the to-do list.")
            self.save_tasks()
        else:
            print("Invalid task index.")
def main():
    todo_list = TodoList()
    while True:
        print("\n1. Display tasks\n2. Add task\n3. Complete task\n4. Delete task\n5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            index = int(input("Enter index of the completed task: "))
            todo_list.complete_task(index)
        elif choice == '4':
            index = int(input("Enter index of the task to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.save_tasks()
            print("Exit, Thankyou!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()