num1 = int(input("type Number 1: "))
num2 = int(input("type Number 2: "))
num3 = int(input("type Number 3: "))

response=0.0

numbers = [num1,num2,num3]

min_value = numbers[0]

for number in numbers[1:]:
    if number < min_value:
        min_value = number

print("Smallest number is {}".format(min_value))