import csv

def simple_csv_analyzer(file_path):
    print(f"Reading: {file_path}")
    rows = 0
    words = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                rows += 1
                words += sum(len(cell.split()) for cell in row)
        
        print(f"Rows: {rows}")
        print(f"Words: {words}")
        
    except FileNotFoundError:
        print("File not found!")

# Get file path
file_path = input("Enter CSV file path: ")
simple_csv_analyzer(file_path)
