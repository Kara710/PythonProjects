import random

#Greetings
print("Welcome to Password Generator Python script")


low_letters="a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
upper_letters = "A  B   C   D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z"

letters = low_letters.split(", ") + upper_letters.split()

number_str="1,2,3,4,5,6,7,8,9"
number_list = number_str.split(",")

special_character_str="@ # $ % ^ & * ( ) _ + | } { ? > <  ="
special_character_list = special_character_str.split()


#print(letters)
#print(number_list)
#print(special_character_list)



num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_special = int(input("How many special characters would you like in your password? "))

password_list=[]

for i in range(0,num_letters):
    password_list += random.choice(letters)

for i in range(0,num_numbers):
    password_list += random.choice(number_list)

for i in range(0,num_special):
    password_list += random.choice(special_character_list)
   
random.shuffle(password_list)

password=""

for char in password_list:
    password += char


print(password)

