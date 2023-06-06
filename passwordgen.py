import random 
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbals = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my PyPassword generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many symbals would you like?\n"))

#easy level
password = ""
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, nr_symbols + 1):
    password += random.choice(symbals)

for char in range(1, nr_numbers):
    password += random.choice(numbers)

print(password) 

#hard level
#to use the shuffle function we need to work wit lists not strings
#that way we can shuffle the order of characters in password
password_list = []
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbals)

for char in range(1, nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

#then to turn the list of random characters back into a string we can use a for loop
random_password = ""
for char in password_list:
    random_password += char #this adds every character in the password_list to the random_password
print(f"Your random password is {random_password}")


     


