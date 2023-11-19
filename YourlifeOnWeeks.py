print("Calculate how many weeks you have if you reached 90 years old")
age = input("What is your current age?")

age_in_int = int(age)
rest_of_years = 90-age_in_int

# A year has 52 weeks
weeks = rest_of_years * 52

message = f"Your remain weeks are: {weeks}"
print(message)