def validate_indian_mobile_number(mobile_number):
    """
    Validates an Indian mobile number according to the following criteria:
    - Must start with 6, 7, 8, or 9
    - Must contain exactly 10 digits
    
    Args:
        mobile_number (str): The mobile number to validate
        
    Returns:
        bool: True if the mobile number is valid, False otherwise
    """
    # Check if the input is a string
    if not isinstance(mobile_number, str):
        return False
    
    # Check if the mobile number starts with valid digits (6, 7, 8, or 9)
    if not mobile_number.startswith(('6', '7', '8', '9')):
        return False
    
    # Check if the mobile number contains exactly 10 digits
    if len(mobile_number) != 10:
        return False
    
    # Check if all characters are digits
    if not mobile_number.isdigit():
        return False
    
    return True


# Taking input from user
if __name__ == "__main__":
    print("Indian Mobile Number Validator")
    print("=" * 30)
    
    # Get input from user
    mobile_number = input("Enter a mobile number: ")
    
    # Validate the input
    is_valid = validate_indian_mobile_number(mobile_number)
    
    # Display the result
    print(f"\nInput: {mobile_number}")
    if is_valid:
        print(f"Result: ✓ VALID - {mobile_number} is a valid Indian mobile number")
    else:
        print(f"Result: ✗ INVALID - {mobile_number} is NOT a valid Indian mobile number")
    
    # Additional validation details
    print(f"\nValidation Details:")
    print(f"- Starts with 6,7,8,9: {'✓' if mobile_number.startswith(('6', '7', '8', '9')) else '✗'}")
    print(f"- Has exactly 10 digits: {'✓' if len(mobile_number) == 10 else '✗'}")
    print(f"- Contains only digits: {'✓' if mobile_number.isdigit() else '✗'}")



    