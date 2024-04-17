DISCOUNT = 0.15
subtotal =float(input("Type the subtotal: "))

if subtotal > 100:
  subtotal = subtotal - (subtotal * DISCOUNT)

print("Subtotal:", subtotal)