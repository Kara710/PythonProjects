# Greetings
print ("Welcome to the tip calculator")

#Total Bill
bill = input("What was the total bill? ")
bill_in_float = float(bill)

#Tip
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_in_int = int(tip)

#Total nmber of people
people = input ("How mamy people to slip the bill? ")
people_in_int= int(people)

cost= ( bill_in_float + (tip_in_int* bill_in_float/100) )/ people_in_int

cost_for_each = round(cost,2)

message = "{:.2f}".format(cost_for_each)

print(f"Each person will pay {message} .")