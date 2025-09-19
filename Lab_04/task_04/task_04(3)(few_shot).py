import csv

def analyze_csv_few_shot(file_path):
    print(f"Analyzing file: {file_path}")
    total_rows = 0
    empty_rows = 0
    total_words = 0
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                total_rows += 1
                if all(col.strip() == "" for col in row):
                    empty_rows += 1
                total_words += sum(len(col.strip().split()) for col in row)
        print(f"Total rows: {total_rows}")
        print(f"Empty rows: {empty_rows}")
        print(f"Total words: {total_words}")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")

# --- Input section
file_path = input("Enter the path to the CSV file: ")
analyze_csv_few_shot(file_path)
