# Escribir un programa que solicite al usuario su nombre y edad.
# Posteriormente, deberá indicarle en qué año cumplirá 100 años.
import datetime
YEARS=100
nombre=input("what's your name? ")
age=int(input("how old are you? "))

today = datetime.date.today()
year = today.year

print(year)
# 2024 + (100 - 35)
new_year= year + (YEARS - age)
print("you'll be 100 years old on the year %s" % new_year)