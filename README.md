# Todo Application

A simple command-line and web API todo application built with Python.

## Features

- **Command Line Interface**: Interactive todo app with menu-driven interface
- **Web API**: RESTful API endpoints for todo management
- **Task Management**: Add, view, complete, and delete tasks
- **Status Tracking**: Visual indicators for task completion

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hello-world.git
   cd hello-world
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Command Line Interface
Run the interactive todo app:
```bash
python file.py
```

#### Web API
Start the Flask API server:
```bash
python todo_api.py
```

The API will be available at `http://localhost:5000`

### API Endpoints

- `GET /` - API information and available endpoints
- `GET /tasks` - Get all tasks
- `POST /tasks` - Add a new task (send JSON with "task" field)
- `PUT /tasks/<id>/complete` - Mark task as complete
- `DELETE /tasks/<id>` - Delete a task

### Example API Usage

```bash
# Get all tasks
curl http://localhost:5000/tasks

# Add a new task
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"task": "Buy groceries"}'

# Mark task as complete
curl -X PUT http://localhost:5000/tasks/1/complete

# Delete a task
curl -X DELETE http://localhost:5000/tasks/1
```

## Project Structure

```
hello-world/
├── file.py          # Command line todo application
├── todo_api.py      # Flask web API
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Contributing

This project is for learning GitHub workflow and Git practices.

## Author

Yousaf Zahid - Created for GitHub and Git learning course.
