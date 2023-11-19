
import random

"""
Theory:
Generate a random word
if user finds a character that part of word, the we add it into the results
if a user type a character that is not part of the word, we will draw part of hangman
if the user enters a number, we will draw part of hangman
it hangman is been full is Game Over



"""

hangman_logo ="""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
___________________________________________________
"""

stages = [ """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 ____|___

""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___
""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___
""",

"""
      _______
     |/      |
     |      (_)
     |      \|
     |      
     |
 ____|___
""",
"""
      _______
     |/      |
     |      (_)
     |      
     |      
     |
 ____|___
""",
"""
      _______
     |/      |
     |      
     |      
     |      
     |
 ____|___
"""
]



#Greetings
print(hangman_logo +"\nWelcome to the Hangman Python script")

word_list = ["lamp","alphabet","dangerously","work","slowly"]
random_word = random.choice(word_list)

print(random_word)

#Print the symbol - for the size of the random_word
display_word = []
for i in range(len(random_word)) :
    display_word +="_"

print("Guess the word: " + str(display_word))

end_of_game = False
lives = 5
letter_not_included="You have already guested : "

while not end_of_game:
    
    #Guess letter
    guess=input("Guess a letter: ").lower()

    
    #Check if the letter is one of the letters in the random_word
    for i in range(len(random_word)) :
        if random_word[i] == guess :
            display_word[i] = guess
            print("Guess the word: " + str(display_word))
    
    #Letter not part of the word
    if guess not in random_word:
        lives -=1
        letter_not_included += guess
        print(letter_not_included )
        if lives == 0 :
            end_of_game = True
            print("You Lose!")
            
    if "_" not in display_word:
        end_of_game = True
        print("You Win!")
    
    print(stages[lives])