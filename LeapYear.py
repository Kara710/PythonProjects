#Greetings
print("Welcome to the Leap Year app")

year=int(input("Enter a year:"))

if (year % 4 == 0 ):
    if ( (year % 100 == 0) & (year % 400 == 0)) :
        print(f"The year {year} is a Leap Year.It has only 266 days")
    elif (year % 100 != 0):
        print(f"The year {year} is a Leap Year.It has only 266 days")
    else:
     print(f"The year {year} is not Leap Year.It has only 265 days")
else:
    print(f"The year {year} is not Leap Year.It has only 265 days")