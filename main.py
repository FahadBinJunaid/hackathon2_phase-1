#!/usr/bin/env python3
"""
Console Todo Application
A simple command-line todo manager with in-memory storage.
"""

from datetime import datetime
import sys
from src.task import Task
from src.task_manager import TaskManager


def display_menu():
    """Display the main menu options."""
    print("\nConsole Todo Application")
    print("========================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark complete")
    print("6. Exit")


def get_user_input(prompt):
    """Get user input with basic error handling."""
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return None
    except EOFError:
        print("\n\nExiting application.")
        return "6"  # Return exit option


def handle_add_task(task_manager):
    """Handle adding a new task."""
    print("\n--- Add New Task ---")

    title = get_user_input("Enter task title: ")
    if title is None:
        return

    if not title.strip():
        print("Error: Task title cannot be empty!")
        return

    description = get_user_input("Enter task description (optional): ")
    if description is None:
        return

    try:
        task = task_manager.add_task(title, description)
        print(f"Task added successfully with ID: {task.id}")
    except ValueError as e:
        print(f"Error: {e}")


def handle_view_tasks(task_manager):
    """Handle viewing all tasks."""
    print("\n--- View All Tasks ---")
    tasks = task_manager.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(task)


def handle_update_task(task_manager):
    """Handle updating a task."""
    print("\n--- Update Task ---")

    task_id_input = get_user_input("Enter task ID to update: ")
    if task_id_input is None:
        return

    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Please enter a valid task ID (number)!")
        return

    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found!")
        return

    print(f"Current task: {task}")

    new_title = get_user_input(f"Enter new title (current: '{task.title}', press Enter to keep current): ")
    if new_title is None:
        return

    new_description = get_user_input(f"Enter new description (current: '{task.description}', press Enter to keep current): ")
    if new_description is None:
        return

    # If user pressed Enter without typing anything, keep the current value
    if new_title == "":
        new_title = None
    if new_description == "":
        new_description = None

    updated_task = task_manager.update_task(task_id, new_title, new_description)
    if updated_task:
        print("Task updated successfully!")
    else:
        print("Failed to update task!")


def handle_delete_task(task_manager):
    """Handle deleting a task."""
    print("\n--- Delete Task ---")

    task_id_input = get_user_input("Enter task ID to delete: ")
    if task_id_input is None:
        return

    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Please enter a valid task ID (number)!")
        return

    # Confirm deletion
    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found!")
        return

    print(f"You are about to delete: {task}")
    confirm = get_user_input("Are you sure? (y/N): ")
    if confirm is None:
        return

    if confirm.lower() in ['y', 'yes']:
        if task_manager.delete_task(task_id):
            print("Task deleted successfully!")
        else:
            print("Failed to delete task!")
    else:
        print("Deletion cancelled.")


def handle_mark_complete(task_manager):
    """Handle marking a task as complete."""
    print("\n--- Mark Task Complete ---")

    task_id_input = get_user_input("Enter task ID to mark complete: ")
    if task_id_input is None:
        return

    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Please enter a valid task ID (number)!")
        return

    task = task_manager.mark_task_complete(task_id)
    if task:
        print("Task marked as complete successfully!")
    else:
        print(f"Error: Task with ID {task_id} not found!")


def main():
    """Main application loop."""
    task_manager = TaskManager()

    print("Welcome to Console Todo Application!")
    print("Type '6' or use Ctrl+C to exit anytime.")

    while True:
        display_menu()

        choice = get_user_input("\nChoose an option (1-6): ")
        if choice is None:
            continue
        elif choice == "6":
            print("\nThank you for using Console Todo Application. Goodbye!")
            break
        elif choice == "1":
            handle_add_task(task_manager)
        elif choice == "2":
            handle_view_tasks(task_manager)
        elif choice == "3":
            handle_update_task(task_manager)
        elif choice == "4":
            handle_delete_task(task_manager)
        elif choice == "5":
            handle_mark_complete(task_manager)
        else:
            print("Invalid option! Please choose a number between 1-6.")

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
