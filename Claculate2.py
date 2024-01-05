print("This program is to calculate the BMI of an individual\n")
name = input("Enter your name: ")
weight = float(input("Enter Your Weight: "))
height = float(input("Enter your height in Meters: "))

bmi = weight / ( height ** 2)

if bmi < 25:
    print(f"{name} is underweight by {bmi} BMI")
else:
    print(f"{name} is overweight by {bmi} BMI")    