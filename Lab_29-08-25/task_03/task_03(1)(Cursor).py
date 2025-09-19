# Modified version with different file names and content
with open("modified_example.txt", "w") as file:
    file.write("Hello, Python World!")
    file.write("\nThis is a modified version!")
    file.write("\nAdding some extra content.")

# Alternative approach with different file handling
filename = "another_file.txt"
content = "Greetings from the modified script!\n"
content += "Today's date: 2024-08-29\n"
content += "File created with Python!"

with open(filename, "w") as output_file:
    output_file.write(content)

print("Files created successfully!")
