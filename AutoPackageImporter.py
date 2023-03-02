"""
This is a script that will scan a directory for Python files and attempt to install all the packages used in those files.
This scans and install packages automatically, so you don't have to manually install them one by one.
Written by: HeavenHM
"""
import argparse
import os
import subprocess

def get_python_files(directory='.'):
    """Returns a list of all Python files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.py')]

def extract_packages_from_files(files):
    """
    Extracts the package names from the import statements in the given list of files.

    Returns a set of package names.
    """
    packages = set()
    for file in files:
        with open(file) as f:
            for line in f:
                if line.startswith('import') or line.startswith('from'):
                    package = line.split()[1]
                    if '.' in package:
                        package = package.split('.')[0]
                    packages.add(package)
    return packages

def remove_system_packages(packages):
    """
    Removes any system packages from the given set of package names.

    Returns a new set with the system packages removed.
    """
    system_packages = set(subprocess.check_output(['pip', 'list', '--format=freeze']).decode().strip().split('\n'))
    return packages - system_packages

def write_packages_to_file(packages, filename='requirements.txt'):
    """
    Writes the given set of package names to a file with the given filename.
    """
    with open(filename, 'w') as f:
        f.write('\n'.join(sorted(packages)))

def install_packages_from_file(filename='requirements.txt'):
    """
    Attempts to install the packages listed in the given file using pip.

    If an error occurs while installing a package, the package is removed from the file
    and the installation process is retried until all packages are successfully installed.
    """
    while True:
        try:
            subprocess.check_call(['pip', 'install', '-r', filename])
            break
        except subprocess.CalledProcessError as e:
            # Remove the package that caused the error
            package = e.cmd[3]
            with open(filename, 'r') as f:
                lines = f.read().splitlines()
            with open(filename, 'w') as f:
                for line in lines:
                    if line != package:
                        f.write(line + '\n')
            print(f"Failed to install {package}, removed it from {filename}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Detect all Python packages used in a directory and install them.')
    parser.add_argument('directory', metavar='DIR', type=str, nargs='?', default='.',
                        help='the directory to scan for Python files (default: current directory)')
    args = parser.parse_args()

    # Get all Python files in the specified directory
    files = get_python_files(args.directory)

    # Extract the package names from the import statements
    packages = extract_packages_from_files(files)

    # Remove system packages
    packages = remove_system_packages(packages)

    # Save the package names to a requirements.txt file
    write_packages_to_file(packages)

    # Install the packages using pip or pip3
    install_packages_from_file()

