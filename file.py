class TodoApp:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task add")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found!")
            return
        
        print("\n=== TO-DO LIST ===")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "□"
            print(f"{i}. [{status}] {task['task']}")
        print()
    
    def mark_complete(self, task_index):
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
    
    def show_menu(self):
        """Display the menu options"""
        print("\n=== TO-DO APP MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        print("=====================")

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