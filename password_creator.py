# This  is a password generator.


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
user_letter = int(input("How many letters would you like in your password?\n"))
user_number = int(input("How many numbers would you like in your password?\n"))
user_symbol =int(input("How many symbols would you like in your password?\n"))


password=[]
for char in range(1,user_letter+1):
    password  += random.choices(letters)
    
for num in range(0,user_number+1):
    password += random.choice(numbers)
        
for sym in range(1,user_symbol+1):
    password += random.choices(symbols)
    


# print(password)
random.shuffle(password)
# to convert the list to string

new_pass = ""
for char in password:
    new_pass+=char

print(f"Your Generated Password is : {new_pass}")





