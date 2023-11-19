#Greetings
print("Welcome to the Python Love Calculator")

#First name 
name1 = input("Enter your name: ")

#Second name 
name2 = input("Enter their name: ")

#We change the variable into lower case
name1_lower= name1.lower()
name2_lower= name2.lower()

name = name1_lower + name2_lower

#We are using the letter of "True Love" to caclulate the percantage

true=0
love=0

true += name.count("t")
true +=  name.count("r")
true +=  name.count("u")
true +=  name.count("e")
love +=  name.count("l")
love +=  name.count("o")
love +=  name.count("v")
love +=  name.count("e")


percantage= int(str(true)+str(love))

if percantage<10 or percantage>90 :
    print(f"Your score is {percantage} , you go together like coke and mentos")
elif percantage>= 40 and percantage<=50 :
    print(f"Your score is {percantage} , you are alright together")
else :
    print(f"Your score is {percantage}.")
