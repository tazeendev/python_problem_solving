# Define special characters
Special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

def password_check_length(password):
    length = len(password) >= 8
    upper = False
    lower = False 
    # main ny idhar variab bnaya ha 
    digit = False
    special = False 

    for char in password:
        if char.isupper():
            upper = True 
        elif char.islower():
            lower = True 
        elif char.isdigit():
            digit = True
        elif char in Special_characters:
            special = True

    if length and upper and lower and digit and special:
        return "Strong password"
    elif length and upper and lower and digit:
        return "Medium password"
    else:
        return "Weak password"

# Take input from user
password = input("Enter your password: ")
result = password_check_length(password)
print("Password strength:", result)
