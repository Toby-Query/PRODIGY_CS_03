import re

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Determine strength based on score
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

def main():
    print("Welcome to the Password Complexity Checker!")
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break

        strength, feedback = check_password_strength(password)

        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions to improve your password:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("Great job! Your password meets all the criteria.")

    print("Thank you for using the Password Complexity Checker!")

if __name__ == "__main__":
    main()