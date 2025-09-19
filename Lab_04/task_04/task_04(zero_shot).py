import csv

def simple_csv_analyzer(file_path):
    row_count = 0
    word_count = 0
    
    print(f"Reading: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            for row in csv_reader:
                row_count += 1
                # Count words in each cell
                for cell in row:
                    words = cell.split()
                    word_count += len(words)
        
        print(f"Rows: {row_count}")
        print(f"Words: {word_count}")
        
    except FileNotFoundError:
        print("File not found!")

# Get file path from user
file_path = input("Enter CSV file path: ")
simple_csv_analyzer(file_path)
