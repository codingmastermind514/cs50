# import
from validator_collection import validators, errors

# try block
try:
    # input
    email_address = validators.email(input("What's your email address? ").strip())# strip
    # print valid
    print("Valid")

# except for nothing or invalid email
except (errors.EmptyValueError, errors.InvalidEmailError):
    # invalid
    print("Invalid")

