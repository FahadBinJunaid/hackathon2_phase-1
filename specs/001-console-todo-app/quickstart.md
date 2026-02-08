# Quickstart Guide: Console Todo Application

## Prerequisites
- Python 3.13 or higher
- Terminal/command prompt access

## Setup
1. Ensure Python 3.13+ is installed on your system
2. Clone or download the project files
3. Navigate to the project directory

## Running the Application
```bash
python main.py
```

## Using the Application

### Main Menu Options
Once the application starts, you'll see the following menu:

```
Console Todo Application
========================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark complete
6. Exit
```

### Adding a Task
1. Select option `1` from the menu
2. Enter a title for the task (required)
3. Optionally enter a description
4. The task will be created with a unique ID and timestamp

### Viewing Tasks
1. Select option `2` from the menu
2. All tasks will be displayed with their ID, title, description, completion status, and creation time

### Updating a Task
1. Select option `3` from the menu
2. Enter the task ID you want to update
3. Enter the new title (or press Enter to keep current title)
4. Enter the new description (or press Enter to keep current description)

### Deleting a Task
1. Select option `4` from the menu
2. Enter the task ID you want to delete
3. Confirm the deletion

### Marking a Task Complete
1. Select option `5` from the menu
2. Enter the task ID you want to mark as complete
3. The task's status will be updated to "completed"

### Exiting the Application
1. Select option `6` from the menu
2. The application will close gracefully

## Error Handling
- Invalid menu selections will show an error message
- Invalid task IDs will show an appropriate error
- Empty titles will be rejected
- The application will not crash on invalid input

## Example Session
```
Console Todo Application
========================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark complete
6. Exit

Choose an option: 1
Enter task title: Buy groceries
Enter task description (optional): Get milk, bread, eggs
Task added successfully with ID: 1

Choose an option: 2
Tasks:
ID: 1 | Title: Buy groceries | Description: Get milk, bread, eggs | Status: Pending | Created: 2026-02-05 10:30:45
```