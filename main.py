import secrets
import string
import random

# Define character sets
letters = string.ascii_letters  # Contains all uppercase and lowercase letters
digits = string.digits  # Contains all digits
special_chars = string.punctuation  # Contains special characters like !, @, #, etc.

# Combine all character sets into one list
selection_list = letters + digits + special_chars

# Take user input for password length
password_len = int(input("Enter password length: "))

# Initialize an empty string to store the password
password = ''

# Generate password of given length
for i in range(password_len):
    # Select a random character from the selection list and add it to the password
    password += ''.join(secrets.choice(selection_list))

# Print the generated password
print(password)
