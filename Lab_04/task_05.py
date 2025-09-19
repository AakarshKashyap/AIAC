import string

# Examples:
# "Hello world! Hello, hello WORLD." → "hello"
# "Apple banana apple, Banana! Fruit." → "apple"
# "The sun shines. The sun rises. Sun." → "sun"

def find_most_frequent_word(text):
    # Convert to lowercase and remove punctuation
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Split into words and count
    words = text.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Find most frequent word
    if word_count:
        return max(word_count, key=word_count.get)
    return None

# Get input and show result
text = input("Enter text: ")
result = find_most_frequent_word(text)

if result:
    print(f"Most frequent word: {result}")
else:
    print("No words found.")
