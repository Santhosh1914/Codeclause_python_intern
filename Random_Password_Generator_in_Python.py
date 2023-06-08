#Random password generator in python task1:
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example
length=int(input("Enter random number: "))
password = generate_password(length)  # Generate a password with length 10
print("password is: ",password)
