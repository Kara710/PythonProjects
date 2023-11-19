height= input("Enter your height in m:")
weight= input("Enter your weight in kg:")

bmi=float(weight)/(float(height)**2)

bmi_as_int=int(bmi)
print(bmi_as_int)

bmi_as_float = float(bmi_as_int)
if (bmi_as_float < 18.5):
    print("Underwaight")
elif (bmi_as_float < 25 ):
    print("Normal weight")
elif (bmi_as_float < 30 ):
    print("Overweight")
elif (bmi_as_float < 35 ):
    print("Obese")
else:
    print("Clinically obese")