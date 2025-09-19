import csv

def analyze_csv_one_shot(file_path):
    print(f"Analyzing file: {file_path}")
    total_rows = 0
    empty_rows = 0
    word_count = 0
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                total_rows += 1
                if not any(cell.strip() for cell in row):
                    empty_rows += 1
                word_count += sum(len(cell.strip().split()) for cell in row)
        print(f"Total rows: {total_rows}")
        print(f"Empty rows: {empty_rows}")
        print(f"Total words: {word_count}")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")

# --- Input section
file_path = input("Enter the path to the CSV file: ")
analyze_csv_one_shot(file_path)
