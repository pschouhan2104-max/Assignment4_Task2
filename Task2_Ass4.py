#Takes user input and writes it to a file named output.txt.
#Appends additional data to the same file.
# Reads and displays the final content of the file.

user_input = input("Enter some text to write to the file: ")
# Write user input to the file
with open("Task2.txt", "w") as file:
    file.write(user_input + "\n")
# Append additional data to the file
with open("Task2.txt", "a") as file:
    file.write("This is additional data appended to the file.\n")
# Read and display the final content of the file
with open("Task2.txt", "r") as file:
    content = file.read()
    print("Final content of the file:")
    print(content)

