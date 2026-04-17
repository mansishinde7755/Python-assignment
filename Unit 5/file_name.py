filename = input("Enter filename: ")

try:
    file = open(filename, "r")
    content = file.read()
    print("\nFile opened successfully!")
    print("File Content:")
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied to read the file.")
