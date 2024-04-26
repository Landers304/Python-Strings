#Task 1: 


def parse_command(user_input):
    commands = {
        "help": "Here are some helpful resources...",
        "issue": "Please describe the issue you're experiencing.",
        "contact support": "You can contact our support team at support@example.com."
    }
    
    # Convert user input to lowercase
    user_input_lower = user_input.lower()
    
    for command, response in commands.items():
        if command in user_input_lower:
            return response
    
    return None

user_input = input("Enter your text input: ")
response = parse_command(user_input)
if response:
    print(response)
else:
    print("No predefined command found.")




#Task 2: 


def categorize_issue(user_input):
    categories = {
        "login": ["login", "signin", "authentication"],
        "performance": ["performance", "slow", "lag", "speed"],
        "error": ["error", "bug", "crash", "exception"],
        "feature request": ["feature request", "enhancement", "new feature"]
    }
    
    # Convert user input to lowercase
    user_input_lower = user_input.lower()
    
    # Check if the user input contains the word "issue"
    if "issue" in user_input_lower:
        # Search through categories and check if any keyword is in user input
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in user_input_lower:
                    return category
    
    return None

user_input = input("Describe the issue: ")
issue_category = categorize_issue(user_input)
if issue_category:
    print("Issue category:", issue_category)
else:
    print("No issue category found.")
