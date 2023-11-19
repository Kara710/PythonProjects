print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************

'''

)

#Greetings
print("Welcome to Treasure Island.\nYour mission is to find the treasure")

way = input("Choose your path, either left or right: ")
way_lower = way.lower()

if way_lower == "right" :
    print("Game Over.")
else :
    choose1 = input("Would you like to wait for the boat or would would prefer to swim? ")
    choose1_lower = choose1.lower()
   
    if choose1_lower == "swim":
        print("Game Over.")
    elif choose1_lower == "wait":
        choose2 = input("Which door you would choose? We have Red, Blue, Yellow: ")
        choose2_lower = choose2.lower()
        
        if choose2_lower== "yellow":
            print("You Win! The treasure is yours....")
        elif choose2_lower == "red":
            print("Game Over. The room is on fire.")
        else:
            print("Game Over. The room is full of the water and you have drown.")
    else:
        print("Game Over. The beast came.")