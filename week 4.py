def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        modified_content = content.upper()
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"File '{input_filename}' has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"Error reading or writing the file: {e}")
input_file = 'input.txt'
output_file = 'output.txt'

modify_file(input_file, output_file)


def read_file_with_error_handling():
    filename = input("Please enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File content of '{filename}':")
        print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError as e:
        print(f"Error: There was an issue reading the file '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
read_file_with_error_handling()
