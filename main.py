import pickle

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, completed=False):
        task = Task(title, description, completed)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{i}. Title: {task.title}, Description: {task.description}, Status: {status}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            print(f"Task '{task.title}' marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            print(f"Task '{task.title}' deleted.")
        else:
            print("Invalid task index.")

    def save_tasks_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)
        print(f"Tasks saved to '{filename}'.")

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
            print(f"Tasks loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except EOFError:
            print("The file is empty or not in the expected format.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add a new task")
        print("2. Display all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save tasks to a file")
        print("6. Load tasks from a file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                title = input("Enter task title: ")
                if title.strip():  # Check if the title is not empty after stripping whitespace
                    break
                else:
                    print("Task title cannot be empty. Please enter a valid title.")

            description = input("Enter task description: ")

            while True:
                completed = input("Is the task completed? (y/n): ").lower()
                if completed in ('y', 'n'):
                    break
                else:
                    print("Invalid input. Please enter 'y' for completed or 'n' for not completed.")

            if completed == 'y':
                task_manager.add_task(title, description, completed=True)
            else:
                task_manager.add_task(title, description)
        elif choice == '2':
            task_manager.display_tasks()
        elif choice == '3':
            task_manager.display_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            task_manager.mark_task_completed(task_index)
        elif choice == '4':
            task_manager.display_tasks()
            task_index = int(input("Enter the index of the task to delete: "))
            task_manager.delete_task(task_index)
        elif choice == '5':
            filename = input("Enter the filename to save tasks: ")
            task_manager.save_tasks_to_file(filename)
        elif choice == '6':
            filename = input("Enter the filename to load tasks: ")
            task_manager.load_tasks_from_file(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()