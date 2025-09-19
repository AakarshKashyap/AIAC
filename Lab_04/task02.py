def factorial(n):
    """
    Calculates the factorial of a number with special handling:
    - Returns 1 for input 0
    - Returns error message for negative numbers
    - Calculates factorial normally for positive numbers
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int or str: Factorial result or error message
    """
    # Handle negative numbers
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    # Handle 0 (special case)
    if n == 0:
        return 1
    
    # Calculate factorial for positive numbers
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


# Taking input from user and displaying results
if __name__ == "__main__":
    print("Factorial Calculator")
    print("=" * 25)
    
    # Get input from user
    try:
        user_input = int(input("Enter a number to calculate factorial: "))
        
        # Calculate factorial
        result = factorial(user_input)
        
        # Display the input and output
        print(f"\nInput: {user_input}")
        print(f"Output: {result}")
        
        # Show detailed calculation for positive numbers
        if user_input > 0:
            print(f"\nCalculation: {user_input}! = ", end="")
            for i in range(1, user_input + 1):
                if i == user_input:
                    print(f"{i}", end="")
                else:
                    print(f"{i} × ", end="")
            print(f" = {result}")
            
    except ValueError:
        print("Error: Please enter a valid integer!")
        