from math import sqrt
a = float(input("type number 1: "))
b = float(input("type number 2: "))
c = float(input("type number 3: "))

def cuadratic(a, b, c):
 d = b**2 - 4*a*c

 if d > 0:
   root1 = (-b + sqrt(d)) / (2*a)
   root2 = (-b - sqrt(d)) / (2*a)
   return (root1, root2)
 elif d == 0:
   root1 = -b / 2*a
   return root1
 else:
   real = -b / 2*a
   imaginary = sqrt(abs(d)) / 2*a
   root1 = complex(real, imaginary)
   root2 = complex(real, -imaginary)
   return (root1, root2)

roots = cuadratic(a, b, c)
print("Roots:", roots)