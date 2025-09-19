import string
from collections import Counter

# Example 1:
# Input: "Hello world! Hello, hello WORLD."
# Output: "hello"

# Example 2:
# Input: "Apple banana apple, Banana! Fruit."
# Output: "apple"

# Example 3:
# Input: "The sun shines. The sun rises. Sun."
# Output: "sun"

def most_frequent_word(paragraph):
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count word frequency
    counts = Counter(words)
    # Return the most common word
    if counts:
        return counts.most_common(1)[0][0]
    else:
        return None

# --- Input section
input_paragraph = input("Enter a paragraph: ")
result = most_frequent_word(input_paragraph)
if result:
    print(f"The most frequently used word is: {result}")
else:
    print("No words found in the input.")
