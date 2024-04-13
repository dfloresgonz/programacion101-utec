# Escribir un programa que reciba una cantidad de minutos y calcule su equivalente en segundos.
CANT_SECS_MIN=60
minutes=int(input("minutes: "))

seconds = minutes * CANT_SECS_MIN
print("there are %s seconds in %s minutes" % (seconds, minutes))