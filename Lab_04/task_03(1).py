def parse_student_info(student_dict):
    """
    Parses student information from nested dictionary
    Returns: "Full Name, Branch, SGPA"
    """
    first_name = student_dict["personal"]["first_name"]
    last_name = student_dict["personal"]["last_name"]
    full_name = f"{first_name} {last_name}"
    
    branch = student_dict["academic"]["branch"]
    sgpa = student_dict["academic"]["sgpa"]
    
    return f"{full_name}, {branch}, {sgpa}"


# Get input from user
if __name__ == "__main__":
    print("Student Information Parser")
    print("=" * 30)
    
    # Take user input
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    branch = input("Enter Branch: ")
    sgpa = float(input("Enter SGPA: "))
    
    # Create student dictionary
    student = {
        "personal": {"first_name": first_name, "last_name": last_name},
        "academic": {"branch": branch, "sgpa": sgpa}
    }
    
    # Display input and output
    print(f"\nInput: {student}")
    result = parse_student_info(student)
    print(f"Output: {result}")