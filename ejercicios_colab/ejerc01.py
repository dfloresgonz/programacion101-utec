# Escribir un programa en Python que permita hallar el área
# y el volumen de una esfera.
# V = 4/3 π r³
import math
radius=4
volume= 4/3 * math.pi * pow(radius, 3)
print("volumne is:", volume)

# 4 π r 2
area=4 * math.pi * pow(radius, 2)
print("area is: %s" % area)
