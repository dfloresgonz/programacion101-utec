num1 = int(input("type Number 1: "))
num2 = int(input("type Number 2: "))

response=""
if num1 > num2:
  response="Number 1 is greater then Number 2"
elif num2 > num1:
  response="Number 2 is greater then Number 1"
elif num1 == num2:
  response="Numbers are equal"

print(response)