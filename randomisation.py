import random

random_int = random.randint(1,10)

print(random_int)

random_float = random.uniform(0,5)

print(random_float)


names_list = input("Enter the names of the people which will partite: ")

names = names_list.split(",")

print(len(names))
random_int2 = random.randint(0,len(names)-1)

print(f"Today the lucky is {names[random_int2]}")

