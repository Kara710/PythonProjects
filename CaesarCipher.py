#Greetings
print("Welcome to Caesar Cipher Python script")

#Alphabet letters
low_letters="a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
letters = low_letters.split(", ")



def ceasar(text , shift , direction ) : 
        new_text = ""
        
        if direction == "encode": 
            for i in text :
                position = letters.index(i)
                new_position = position + shift
                if new_position > 25 :
                    start = new_position-26
                    new_text += letters[start]
                else:
                    new_text += letters[new_position]
                    
            print(f"Here's the encoded results: {new_text}")
        else :
            for i in text :
                position = letters.index(i)
                new_position = position - shift 
                new_text += letters[new_position]
            
            print(f"Here's the decoded results: {new_text}")
            
choise2=True          
while ( choise2 ) :
    choise = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    ceasar(message,shift,choise)
    choise2 =input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if choise2 == "no" :
        choise2=False

