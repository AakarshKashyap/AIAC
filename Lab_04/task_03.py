def parse_student_info(student: dict) -> str:
    """
    Extracts Full Name, Branch, and SGPA from a nested student dictionary.
    Returns a formatted string: "FullName, Branch, SGPA"
    """
    first_name = student.get("personal", {}).get("first_name", "")
    last_name = student.get("personal", {}).get("last_name", "")
    branch = student.get("academic", {}).get("branch", "")
    sgpa = student.get("academic", {}).get("sgpa", "")

    full_name = f"{first_name} {last_name}".strip()
    return f"{full_name}, {branch}, {sgpa}"


# 🔹 Taking inputs from user
student = {
    "personal": {
        "first_name": input("Enter first name: "),
        "last_name": input("Enter last name: ")
    },
    "academic": {
        "branch": input("Enter branch: "),
        "sgpa": float(input("Enter SGPA: "))
    }
}

# 🔹 Printing extracted details
print("Student Details:", parse_student_info(student))
