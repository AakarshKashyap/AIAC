# Modified version - convert text to lowercase
with open("source.txt", "r") as input_file, open("result.txt", "w") as output_file:
    for line in input_file:
        output_file.write(line.lower())

print("Text converted to lowercase successfully!")
