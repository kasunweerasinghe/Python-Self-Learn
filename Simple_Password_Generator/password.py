import random

# Letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get USer Inputs Data
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

password = ""

# for get random letters
for char in range(1, nr_letters):
    password += random.choice(letters)

# for get random symbols
for char in range(1, nr_symbols):
    password += random.choice(symbols)

# for get random numbers
for char in range(1, nr_numbers):
    password += random.choice(numbers)

# print the password
print(password)