def modify_file_content(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        modified_content = content.upper()

        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"File processed successfully. Output saved to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except IOError:
        print("Error: There was an issue reading or writing the file.")

filename = input("Enter the name of the file to read from: ")
output_filename = "modified_output.txt"

modify_file_content(filename, output_filename)
