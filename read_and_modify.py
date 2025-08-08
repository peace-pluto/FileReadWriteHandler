def read_and_modify_file():
    try:
        # Ask user for the file name
        filename = input("Enter the name of the file to read: ")

        # Try opening the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Create a new file name for the modified file
        new_filename = "modified_" + filename

        # Write modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except IOError:
        print("❌ Error: There was a problem reading the file.")

# Run the function
read_and_modify_file()