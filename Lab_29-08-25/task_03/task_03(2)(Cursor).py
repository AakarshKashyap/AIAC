# Simple version - opening two files simultaneously
with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("Content for first file\n")
    f2.write("Content for second file\n")

print("Files created successfully!")
