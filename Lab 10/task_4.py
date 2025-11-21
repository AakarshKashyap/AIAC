def welcome_student(name: str) -> None:
    """
    Print a welcome message for a single student.
    
    Args:
        name (str): The student's name.
    """
    print("Welcome", name)


def welcome_all_students(students: list[str]) -> None:
    """
    Print welcome messages for all students in the list.
    
    Args:
        students (list[str]): List of student names.

    Returns:
        None

    Raises:
        TypeError: If students is not a list of strings.
    """
    if not isinstance(students, list):
        raise TypeError("Students must be a list of strings.")

    for student in students:
        welcome_student(student)


# Example usage
students = ["Alice", "Bob", "Charlie"]
welcome_all_students(students)
