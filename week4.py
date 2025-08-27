# File Read & Write Challenge with Error Handling 

def main():
    # Step 1: Ask user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Step 2: Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()

        # Step 3: Modify the content (convert to uppercase as an example)
        modified_content = content.upper()

        # Step 4: Create a new file to save the modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f" File processed successfully! Modified content saved in '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
