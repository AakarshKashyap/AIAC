with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
    for line in inp:
        outp.write(line.upper())

print("Processing done")