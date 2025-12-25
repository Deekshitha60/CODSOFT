import random
import string

def generate_password(length):
    # Characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter the desired password length: "))

# Generate and display password
password = generate_password(length)
print("Generated Password:", password)