#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for n in range(0,nr_letters):
  password = random.choices(letters,k=nr_letters)
for n in range(0,nr_symbols):
  password.append(random.choice(symbols))
for n in range(0,nr_numbers):
  password.append(random.choice(numbers))
''.join(password)

#Convert simple password list into string
simp_pass = ""
for char in password:
  simp_pass += char
print(f"Your simple password is: {simp_pass}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_pass = (random.sample(password,len(password)))
''.join(random_pass)

#Convert random password list into string
hard_pass = ""
for char in random_pass:
  hard_pass += char
print(f"Your strong, random password is: {hard_pass}")