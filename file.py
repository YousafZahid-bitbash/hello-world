import json
import os

class TodoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from the JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    
    def save_tasks(self):
        """Save tasks to the JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        # Save tasks after adding a new one
        print(f"✅ Task successfully added: '{task}'")
    
    # BEGIN: view_tasks
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found.")
            return
        for index, task in enumerate(self.tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            due_date = f" (Due: {task['due_date']})" if task['due_date'] else ""
            print(f"{index}. {task['task']} [{status}]{due_date}")
    # END: view_tasks
    
    #function to sort tasks by due date
    def sort_tasks_by_due_date(self):
        """Sort tasks by due date"""
        self.tasks.sort(key=lambda x: x['due_date'] if x['due_date'] else "")
    
    #function to mark a task as complete
    def mark_complete(self, task_num):
        """Mark a task as complete"""
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task marked as complete: {self.tasks[task_index - 1]['task']}")
        else:
            print("Invalid task number!")
    
    def delete_task(self, task_index):
        """Delete a task"""
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task deleted: {deleted_task['task']}")
        else:
            print("Invalid task number!")


    



def main():
    todo_app = TodoApp()
    
    print("Welcome to the Simple To-Do Application!")
    
    while True:
        todo_app.show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                todo_app.add_task(task)
            else:
                print("Task cannot be empty!")
        
        elif choice == "2":
            todo_app.view_tasks()
        
        elif choice == "3":
            todo_app.view_tasks()
            try:
                task_num = int(input("Enter task number to mark as complete: "))
                todo_app.mark_complete(task_num)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "4":
            todo_app.view_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                todo_app.delete_task(task_num)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "5":
            print("Thank you for using the To-Do App!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()