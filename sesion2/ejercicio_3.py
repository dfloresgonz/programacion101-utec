import math
number = 567 #input("type your 3 digit number: ")

first = number // 100
print("First number: ", first)

rest = number % 100

second = rest // 10
print("second number: ", second)
rest = number % 10

third = rest
print("third number: ", third)

last = (third * 100) + (second*10) + first
print("last number: ", last)
