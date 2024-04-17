num1 = int(input("type Number 1: "))
num2 = int(input("type Number 2: "))

response = num1 % num2

if response > 0:
  print(f"{num1} is not divisible by {num2}")
else:
  print(f"{num1} is divisible by {num2}")
