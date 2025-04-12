# todo.py
"""
A simple command-line To-Do List application that allows users to manage tasks.
"""

from typing import List
from datetime import date

class Task:
    def __init__(self, name):
        self.name = name
        self.date_created = date.today()

    def __str__(self):
        return f"{self.name} (created on {self.date_created})"


class Todo:
    """A simple To-Do list application that manages tasks in memory.

    This class provides basic task management functionality including adding,
    deleting, and viewing tasks. Tasks are stored in memory as a list.
    """

    def __init__(self) -> None:
        """Initialize a new Todo instance with an empty task list."""
        self.tasks: List[str] = []

    def add_task(self, task: str) -> None:
        """Add a new task to the list.

        Args:
            task: The task description to add.

        Note:
            Prints a success message if the task is added,
            or an error message if the task is empty.
        """
        if task:
            newTask = Task(task)
            self.tasks.append(newTask)
            print(f"Task '{newTask.name}' added successfully.")
        else:
            print("Task cannot be empty.")

    def delete_task(self, task: str) -> None:
        """Delete a task from the list.

        Args:
            task: The task description to delete.

        Note:
            Prints a success message if the task is deleted,
            or an error message if the task is not found.
        """
        for t in self.tasks:
            if t.name == task:
                self.tasks.remove(t)
                print(f"Task '{task}' deleted successfully.")
                return 
        print(f"Task '{task}' not found.")

    def show_tasks(self) -> None:
        """Display all current tasks in a numbered list.

        Note:
            Prints a message if there are no tasks,
            or a numbered list of all tasks if any exist.
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task.date_created} {task.name}")


def main():
    """Run the interactive To-Do list application.

    This function provides a command-line interface for interacting
    with the Todo class. It continuously prompts the user for actions
    until they choose to quit.
    """
    todo = Todo()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Quit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            task = input("Enter the task to delete: ")
            todo.delete_task(task)
        elif choice == "3":
            todo.show_tasks()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
