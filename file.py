class TodoApp:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task, due_date=None):
        """Add a new task to the list with an optional due date"""
        self.tasks.append({"task": task, "completed": False, "due_date": due_date})
        print(f"✅ Task successfully added: '{task}' with due date: '{due_date}'")
    
    # BEGIN: view_tasks
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks available.")
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
        if 0 < task_num <= len(self.tasks):
            self.tasks[task_num - 1]["completed"] = True
            print(f"✅ Task {task_num} marked as complete.")
        else:
            print("Invalid task number!")
    
    #function to delete a task
    def delete_task(self, task_num):
        """Delete a task from the list"""
        if 0 < task_num <= len(self.tasks):
            removed_task = self.tasks.pop(task_num - 1)
            print(f"✅ Task '{removed_task['task']}' deleted successfully.")
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