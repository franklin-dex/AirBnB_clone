# HBNB - THE CONSOLE

## Description
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

## Command Interpreter

The command interpreter is a CLI tool that allows users to interact with the AirBnB clone project from the command line. It provides various commands to manage accommodations, users, bookings, and other aspects of the platform.

### Starting the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the directory containing the project files.
3. Run the command `python3 console.py` to start the command interpreter.

### Using the Command Interpreter

Once the command interpreter is running, you can use the following commands:

- `create`: Creates a new instance of a specified class (e.g., `create BaseModel`).
- `show`: Displays details of a specific instance (e.g., `show BaseModel 1234`).
- `destroy`: Deletes a specific instance (e.g., `destroy BaseModel 1234`).
- `update`: Updates attributes of a specific instance (e.g., `update BaseModel 1234 name "New Name"`).
- `all`: Displays details of all instances or instances of a specific class (e.g., `all BaseModel`).
- `quit` or `EOF`: Exits the command interpreter.

### Examples

```bash
$ python3 console.py
(hbnb) create BaseModel
12121212-1234-5678-9876-543211223344
(hbnb) show BaseModel 12121212-1234-5678-9876-543211223344
[BaseModel] (12121212-1234-5678-9876-543211223344) {'id': '12121212-1234-5678-9876-543211223344', 'created_at': datetime.datetime(2022, 2, 22, 12, 0, 0), 'updated_at': datetime.datetime(2022, 2, 22, 12, 0, 0)}
(hbnb) all
["[BaseModel] (12121212-1234-5678-9876-543211223344) {'id': '12121212-1234-5678-9876-543211223344', 'created_at': datetime.datetime(2022, 2, 22, 12, 0, 0), 'updated_at': datetime.datetime(2022, 2, 22, 12, 0, 0)}"]
(hbnb) quit
$

