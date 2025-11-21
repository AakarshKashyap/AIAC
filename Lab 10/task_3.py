def calculate_percentage(amount: float, percentage: float) -> float:
    """
    Calculate the given percentage of an amount.

    Args:
        amount (float): The base amount.
        percentage (float): The percentage to calculate.

    Returns:
        float: The calculated percentage of the amount.

    Raises:
        ValueError: If percentage is negative.
    """
    if percentage < 0:
        raise ValueError("Percentage must be non-negative.")
    return amount * percentage / 100

if __name__ == "__main__":
    amount = 200
    percentage = 15
    result = calculate_percentage(amount, percentage)
    print(f"{percentage}% of {amount} is {result}")
