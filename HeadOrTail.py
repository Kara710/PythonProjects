import random

#Greetings
print("Welcome to Heads or Tails Python script")

random_int=random.randint(0,1)

if random_int == 1 :
    #Heads
    print( """
      _                    _ 
| |                  | |
| |__   ___  __ _  __| |
| '_ \ / _ \/ _` |/ _` |
| | | |  __/ (_| | (_| |
|_| |_|\___|\__,_|\__,_|
    
    """
    )
    
else:
    #Tails
    
    print("""
_        _ _ 
| |      (_) |
| |_ __ _ _| |
| __/ _` | | |
| || (_| | | |
 \__\__,_|_|_|
    
    
    """
    