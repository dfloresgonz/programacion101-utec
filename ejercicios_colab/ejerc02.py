# Escribir un programa en Python que permita ingresar un monto en soles y
# muestre su equivalente en dólares y euros.
TIPO_CAMBIO=3.7

soles=100
dolares = soles / TIPO_CAMBIO
print("dolares: %s" % dolares)

dolares_amount=100
soles= dolares_amount * TIPO_CAMBIO
print("soles: %s" % soles)