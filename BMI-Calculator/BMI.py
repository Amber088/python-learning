weight = float(input("Enter your weight in kg : "))
height = float(input ("Enter your height in m : "))
BMI = (weight) / ((height * height))
if(BMI < 18.5):
    print(BMI,"UnerWeight")
elif (BMI >= 18.5 and BMI <= 24.9):
    print(BMI, "Normal weight")
elif (BMI > 24.9 and BMI < 30):
    print(BMI, "Overweight")
else:
    print(BMI, "Obese")

