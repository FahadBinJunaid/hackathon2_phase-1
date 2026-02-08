# Console Todo Application

A simple command-line todo manager with in-memory storage, built with Python.

## Features

- Add tasks with titles and optional descriptions
- View all tasks with details (ID, title, description, status, creation timestamp)
- Update task details by ID
- Delete tasks by ID
- Mark tasks as complete
- Clean, user-friendly console interface
- Robust error handling and input validation

## Prerequisites

- Python 3.13 or higher

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies (if any) using:
   ```bash
   pip install -e .
   ```

## Usage

Run the application using:
```bash
python main.py
```

The application presents a menu-driven interface:

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

### Menu Options

1. **Add task**: Create a new task with a required title and optional description
2. **View tasks**: Display all tasks with their details
3. **Update task**: Modify an existing task's title or description by ID
4. **Delete task**: Remove a task by ID (with confirmation)
5. **Mark complete**: Mark a task as completed by ID
6. **Exit**: Close the application gracefully

## Example Session

```
Welcome to Console Todo Application!
Type '6' or use Ctrl+C to exit anytime.

Console Todo Application
========================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark complete
6. Exit

Choose an option (1-6): 1

--- Add New Task ---
Enter task title: Buy groceries
Enter task description (optional): Get milk, bread, eggs
Task added successfully with ID: 1

Press Enter to continue...
```

## Architecture

The application consists of:

- `main.py`: Entry point and CLI interface
- `src/task.py`: Task model representing individual todo items
- `src/task_manager.py`: Task management with in-memory storage
- `pyproject.toml`: Project configuration and dependencies

## Error Handling

The application includes comprehensive error handling for:
- Invalid menu selections
- Invalid task IDs (non-numeric input)
- Non-existent task IDs
- Empty task titles
- Keyboard interrupts (Ctrl+C)

The application will not crash on invalid input and provides appropriate error messages.

## Data Model

Each task contains:
- `id`: Auto-incrementing integer identifier
- `title`: Required string (cannot be empty)
- `description`: Optional string (can be empty)
- `completed`: Boolean status (default: False)
- `created_at`: Timestamp of when the task was created

## Development

To run the application in development mode:
```bash
python main.py
```

## License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.