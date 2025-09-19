def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Get input from user
user_input = int(input("Enter a number: "))
output = factorial(user_input)
print(f"Input: {user_input} → Output: {output}")