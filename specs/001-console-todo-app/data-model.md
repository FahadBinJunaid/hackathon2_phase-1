# Data Model: Console Todo Application

## Entity: Task

### Fields
- **id** (Integer)
  - Type: Auto-incrementing integer
  - Required: Yes
  - Constraints: Unique within session
  - Description: Unique identifier for each task

- **title** (String)
  - Type: String
  - Required: Yes
  - Constraints: Non-empty, minimum 1 character
  - Description: Task title/description

- **description** (String)
  - Type: String
  - Required: No
  - Constraints: Optional, can be null/empty
  - Description: Optional detailed description of the task

- **completed** (Boolean)
  - Type: Boolean
  - Required: Yes
  - Constraints: True/False values only
  - Description: Status indicating if task is completed

- **created_at** (DateTime)
  - Type: Timestamp
  - Required: Yes
  - Constraints: Automatically set on creation
  - Description: Date/time when task was created

### Relationships
- No relationships needed (standalone entity)

### Validation Rules
- Title must be provided and not empty
- ID must be unique within the current session
- Created timestamp automatically set when task is created
- Completed status defaults to False

### State Transitions
- `completed = False` → `completed = True` (when user marks task as complete)
- No other state transitions required

## Entity: Task List

### Description
- Collection of Task entities stored in memory
- Maintains order of insertion
- Provides methods for CRUD operations

### Operations
- Add new Task to list
- Retrieve all Tasks from list
- Find Task by ID
- Update Task in list
- Remove Task from list
- Count total Tasks in list

### Constraints
- All IDs within list must be unique
- List exists only for duration of application session
- No persistence outside of session