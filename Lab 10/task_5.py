# Optimized code using list comprehension
import time # Importing time module for performance measurement
start_time = time.time() # Start time measurement
squares = [n**2 for n in range(1, 1000000)] # List comprehension for efficiency
end_time = time.time() # End time measurement
print(len(squares)) # Print the length of the list to verify
print(f"Time taken: {end_time - start_time} seconds") # Print the time taken for the operation