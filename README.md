# AutoPackageImporter
The Python Package Detector is a tool that detects all Python packages used in a directory, removes any system packages from the list, saves the list to a requirements.txt file, and installs all the detected packages using pip or pip3. This helps developers manage dependencies for their Python projects, ensuring that all developers have the same dependencies installed, reducing the risk of compatibility issues and bugs, and creating a consistent and repeatable installation process that can be automated or easily run on multiple systems.

## Prerequisites

- Python 3.x
- pip or pip3

## Installation

Clone this repository and navigate to the cloned directory.
This will detect all Python packages used in the specified directory and install them using pip or pip3.


## Usage

- `<directory>` (optional): the directory to scan for Python files (default: current directory)

## Example

python AutoPackageImporter.py /path/to/directory

## Features

- Automatically detects all Python packages used in a directory, saving time and effort.
- Removes system packages from the list of detected packages, preventing unnecessary installations.
- Saves the list of detected packages to a `requirements.txt` file for future installations or sharing with other developers.
- Automatically installs all detected packages using pip or pip3, ensuring that all dependencies are met.

## Use Cases

- Managing dependencies for Python projects of any size or complexity.
- Ensuring that all developers working on a project have the same dependencies installed, reducing the risk of compatibility issues and bugs.
- Creating a consistent and repeatable installation process that can be automated or easily run on multiple systems.
- Helping developers keep track of which packages they are using and why, making it easier to maintain and update projects over time.

## License

This project is licensed under the MIT License. See `LICENSE` for more information.



