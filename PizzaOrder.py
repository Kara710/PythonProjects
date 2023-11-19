#Greetings
print("Welcome to Python Pizza Deliveries!")

#Size of pizza
size= input("What size pizza do you want? S, M ,L  :")

#Extra ingredients
add_pepperoni = input("Do you want pepperoni? Y, N  :")
add_cheese = input("Do you want extra cheese? Y, N  :")

# Total prize
prize=0;

if ( size == "S"):
    prize=15
elif ( size == "M"):
    prize=20
elif ( size == "L"):
    prize=25

if add_pepperoni == "Y" :
    if size == "S":
        prize +=2
    else:
        prize +=3

               
if( add_cheese == "Y"):
    prize +=1
    
print ( f"The price for your pizza {size} is {prize}" )