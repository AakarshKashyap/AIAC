def calc_average(marks: list[int]) -> float:
    """
    Calculate the average score of a student.

    Args:
        marks (list[int]): A list of integer scores.

    Returns:
        float: The average of the scores.

    Raises:
        ValueError: If the marks list is empty.
    """
    if not marks:
        raise ValueError("Marks list is empty")

    total = 0
    for m in marks:
        total += m
    average = total / len(marks)  # Corrected typo: 'avrage' → 'average'
    return average


# Example usage
marks = [85, 90, 78, 92]
print("Average Score is", calc_average(marks))  # Fixed missing parenthesis