#Task 1: 


def validate_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name should be at least 2 characters long.")
    else:
        print("Names are valid.")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

validate_name_length(first_name, last_name)




#Task 2:


def check_password_complexity(password):
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
    
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    
    # If criteria is met, password is sufficient
    print("Password complexity is sufficient.")
    return True

password = input("Enter your password: ")
check_password_complexity(password)




#Task 3: 


import re

def format_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches pattern
    if re.match(email_pattern, email):
        # Convert the email to lowercase
        formatted_email = email.lower()
        return formatted_email
    else:
        print("Invalid email format. Please enter a valid email address.")
        return None

email = input("Enter your email address: ")
formatted_email = format_email(email)
if formatted_email:
    print("Formatted email:", formatted_email)
