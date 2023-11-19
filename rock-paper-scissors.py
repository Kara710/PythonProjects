import random

#Greetings
print("Welcome to the Rock Paper Scissors Python script")


#Declare variables

rock="""

      .-.___
 ----/ \()__)
   (  (/()__)
        ()__)
----\___()_)
"""

paper="""

      .-.___
 ----/ \ )____)
   (  (/ )_____)
         )____)
----\___ )___)

"""


scissors ="""

      .-.___
 ----/ \ )______)
   (  (/ )______)
        ()__)
----\___()_)

"""

list_options=[rock,paper,scissors]

chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_chose = random.randint(0,2)

print(list_options[chose]+"\n Computer chose: \n" + list_options[computer_chose] )


if chose == 0 and computer_chose == 2 :
    print("You Win!")
elif chose == 2 and computer_chose == 1 :
    print("You Win!")
elif chose == 1 and computer_chose == 0 :
    print("You Win!")
elif chose == computer_chose :
    print("Tie, none Wins")
else:
    print("Computer Wins!")