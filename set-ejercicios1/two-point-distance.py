x1 = int(input("type Number 1: "))
y1 = int(input("type Number 2: "))
x2 = int(input("type Number 3: "))
y2 = int(input("type Number 4: "))

distance = ((x2-x1)**2) + ((y2-y1)**2)

distance = distance**0.5 #square root o raiz cuadrada
distance = round(distance, 2)

print("The distance is: ", distance)