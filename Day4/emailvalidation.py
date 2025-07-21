import re
def valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
email = input("Enter your email: ")

if valid_email(email):
    print("Valid email")
else:
    print("Invalid email")
