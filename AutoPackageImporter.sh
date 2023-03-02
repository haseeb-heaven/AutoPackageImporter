#!/bin/bash

# Function to get all Python files in the specified directory
get_python_files() {
    directory="$1"
    find "$directory" -name "*.py"
}

# Function to extract the package names from the import statements in the given files
extract_packages_from_files() {
    files="$1"
    packages=$(grep -E "^import|^from" $files | sed -E "s/import |from | .*//g" | sed -E "s/\..*//g" | sort -u)
    echo "$packages"
}

# Function to remove any system packages from the given set of package names
remove_system_packages() {
    packages="$1"
    system_packages=$(pip list --format=freeze | grep -E "^package==" | sed -E "s/^package==//g")
    packages=$(echo "$packages" | grep -vFx "$system_packages")
    echo "$packages"
}

# Function to write the given set of package names to a file with the given filename
write_packages_to_file() {
    packages="$1"
    filename="$2"
    echo "$packages" > "$filename"
}

# Function to install the packages listed in the given file using pip or pip3
install_packages_from_file() {
    filename="$1"
    while read -r package; do
        if [[ -n "$package" ]]; then
            pip install "$package"
        fi
    done < "$filename"
}

# Main function
main() {
    directory="${1:-.}"

    # Get all Python files in the specified directory
    files=$(get_python_files "$directory")

    # Extract the package names from the import statements
    packages=$(extract_packages_from_files "$files")

    # Remove system packages
    packages=$(remove_system_packages "$packages")

    # Save the package names to a requirements.txt file
    write_packages_to_file "$packages" "requirements.txt"

    # Install the packages using pip or pip3
    install_packages_from_file "requirements.txt"
}

main "$@"
