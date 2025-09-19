import csv

def analyze_csv(file_path):
    total_rows = 0
    empty_rows = 0
    total_words = 0
    print(f"Analyzing file: {file_path}")

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                total_rows += 1
                # Check if all cells in the row are empty after stripping whitespace
                if all(cell.strip() == '' for cell in row):
                    empty_rows += 1
                # Count words in all cells
                for cell in row:
                    words = cell.strip().split()
                    total_words += len(words)

        print(f"Total rows: {total_rows}")
        print(f"Empty rows: {empty_rows}")
        print(f"Total words: {total_words}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")

# Ask user for input
file_path = input("Enter the path to the CSV file: ")
analyze_csv(file_path)
