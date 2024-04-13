weight=int(input("Type your weight in grams: "))
height=int(input("Type your height in centimeters: "))

bmi = (weight/1000) / pow( (height/100), 2)
bmi = round(bmi, 3)
print("BMI is: ", bmi)