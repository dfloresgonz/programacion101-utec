# Escriba un programa que reciba un número representando una cantidad de segundos.
# Posteriormente, el programa deberá calcular cuantos minutos y segundos hay en ese tiempo.
# Por ejemplo: 150 segundos -> 2 minutos 30 segundos.

import math
CANT_SECS_MIN=60

seconds=int(input("seconds: "))

minutes = seconds / CANT_SECS_MIN

secs_decimal = minutes % 1 # get the decimal part of the division (for seconds)
secs = CANT_SECS_MIN * secs_decimal # transform decimal to seconds
minutes = math.floor(minutes) # get the whole part of the division (minutes)

print("mins: %s, secs: %s" % (minutes, secs ) )