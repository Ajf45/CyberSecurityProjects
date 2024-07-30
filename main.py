import re

def password_strength_checker(password):
    """
    Evaluates the strength of a given password.

    Args:
        password (str): The password to evaluate.

    Returns:
        tuple: A tuple containing the password strength score and suggestions for improvement.
    """
    # Initialize score and suggestions
    score = 0
    suggestions = []

    # Check length
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    else:
        score += 1

    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        suggestions.append("Password should contain at least one uppercase letter.")
    else:
        score += 1

    # Check for lowercase letters
    if not re.search("[a-z]", password):
        suggestions.append("Password should contain at least one lowercase letter.")
    else:
        score += 1

    # Check for numbers
    if not re.search("[0-9]", password):
        suggestions.append("Password should contain at least one number.")
    else:
        score += 1

    # Check for special characters
    if not re.search("[^A-Za-z0-9]", password):
        suggestions.append("Password should contain at least one special character.")
    else:
        score += 1

    # Determine password strength based on score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions

def main():
    password = input("Enter a password: ")
    strength, suggestions = password_strength_checker(password)
    print(f"Password strength: {strength}")
    if suggestions:
        print("Suggestions for improvement:")
        for suggestion in suggestions:
            print(suggestion)

if __name__ == "__main__":
    main()