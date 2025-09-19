def validate_indian_mobile(number: str) -> bool:
    """
    Validates an Indian mobile number.
    Conditions:
    - Must contain exactly 10 digits.
    - Must start with 6, 7, 8, or 9.
    """
    return number.isdigit() and len(number) == 10 and number[0] in "6789"


# 🔹 Taking input from user
mobile_number = input("Enter a mobile number: ")

if validate_indian_mobile(mobile_number):
    print(f"{mobile_number} is a valid Indian mobile number ✅")
else:
    print(f"{mobile_number} is NOT a valid Indian mobile number ❌")
