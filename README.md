
# Task Manager App

## Description
The Task Manager App is a simple command-line application designed to help you manage tasks effectively. It supports creating, updating, and saving tasks, as well as notifying users about task updates. The app is built using Python and incorporates file I/O operations to store tasks persistently.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/theemani/task_manager_app.git
   cd task-manager-app
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the main script:**
   ```bash
   python main.py
   ```

2. **Example Output:**
   ```
   Task Created: New Task - Description of the new task
   Notification: A new task has been created!
   Task Updated: New Task - Description of the new task - Status: completed
   Notification: Task has been updated!
   ```

## Features

- Create new tasks with a unique ID, name, description, and status.
- Update existing tasks' name, description, and status.
- Notify users about task updates.
- Save tasks to a JSON file for persistence.
- Load tasks from a JSON file at startup.
- Unit tests for the `Task` and `TaskManager` classes.

## Project Structure

```plaintext
task-manager-app/
│
├── task_manager/
│   ├── __init__.py
│   ├── file_manager.py
│   ├── task.py
│   └── task_manager.py
│
├── tests/
│   ├── __init__.py
│   ├── test_task.py
│   └── test_task_manager.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. Ensure that your code follows the existing style and passes all tests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

Created by [Manuel Oni](https://github.com/theemani) - feel free to contact me!

## Acknowledgements

- Inspiration from various task management applications.
```

### Explanation:

1. **Project Title and Description**: States the project name and provide a brief description of what it does.
2. **Table of Contents**: Helps in navigating the README easily.
3. **Installation**: Step-by-step instructions to set up the project locally.
4. **Usage**: Instructions on how to run the application and example output.
5. **Features**: Highlights the main features of the application.
6. **Project Structure**: Provides an overview of the directory structure and file organization.
7. **Contributing**: Guidelines for how others can contribute to the project.
8. **License**: Information about the project’s license.
9. **Contact**: Contact information for the project maintainer.
10. **Acknowledgements**: Credit to inspirations and assistance.

Feel free to adjust the content to better suit your project's specifics and personal preferences.
