weight_kg=float(input("Type the weight in kilograms: "))
height_mt=float(input("Type the height in meters: "))

imc = weight_kg / pow(height_mt, 2)
imc = round(imc, 2)
print("The IMC is", imc)