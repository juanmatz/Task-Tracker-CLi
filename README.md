# Task Tracker CLI 📝

An efficient Command Line Interface (CLI) application to manage and track your daily tasks. This project is built with Python and uses JSON data persistence to ensure you never lose your progress.

## 🚀 Features

- **Create Tasks:** Add new tasks with custom descriptions.
- **Update Status:** Mark tasks as "In Progress" or "Done".
- **Data Persistence:** All tasks are automatically saved to a `datos.json` file. Your data survives program restarts!
- **View Filters:**
  - View all tasks.
  - View only tasks in progress.
  - View only completed tasks.
- **Smart ID Management:** Automatic incremental ID system that avoids duplicates.

## 🛠️ Technologies Used

- **Python 3**: Core language.
- **JSON**: For local data storage.
- **OOP (Object-Oriented Programming)**:
  - [Task.py](cci:7://file:///c:/Users/juanm/Documents/python/Task%20Tracker%20Project/Task.py:0:0-0:0): Class defining the task object (Model).
  - [Todo.py](cci:7://file:///c:/Users/juanm/Documents/python/Task%20Tracker%20Project/Todo.py:0:0-0:0): Controller class handling list logic and database operations.
  - [Main.py](cci:7://file:///c:/Users/juanm/Documents/python/Task%20Tracker%20Project/Main.py:0:0-0:0): User interface and main menu.

## 📋 Requirements

- Python 3.x installed on your system.

## 💻 How to Run

1.  Clone this repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Task-Tracker-CLI.git](https://github.com/YOUR_USERNAME/Task-Tracker-CLI.git)
    ```
2.  Navigate to the project folder:
    ```bash
    cd "Task Tracker Project"
    ```
3.  Run the application:
    ```bash
    python Main.py
    ```

## 📂 Project Structure


```text
Task Tracker Project/
│
├── Main.py      # Entry point and user menu
├── Todo.py      # List management logic and JSON saving
├── Task.py      # Task class definition
└── datos.json   # Database (created automatically)
```
## Project URL [https://github.com/juanmatz/Task-Tracker-CLi](https://roadmap.sh/projects/task-tracker)


