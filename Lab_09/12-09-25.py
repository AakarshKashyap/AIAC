def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a given list.

    Args:
        numbers (list of int): The list of integers to process.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.

    Example:
        >>> sum_even_odd([1, 2, 3, 4])
        (6, 4)
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum
# Example of how to use the function and get output
numbers_list = [1, 2, 3, 4]
even_sum, odd_sum = sum_even_odd(numbers_list)

# Print the result
print(f"The sum of even numbers is: {even_sum}")
print(f"The sum of odd numbers is: {odd_sum}")
print(f"The full result is: ({even_sum}, {odd_sum})")