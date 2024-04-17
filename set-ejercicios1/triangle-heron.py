from math import sqrt
s1 = int(input("type side 1: "))
s2 = int(input("type side 2: "))
s3 = int(input("type side 3: "))

semiperimeter = (s1 + s2 + s3) / 2

area = sqrt(semiperimeter * (semiperimeter - s1) * (semiperimeter - s2) * (semiperimeter - s3) )

print("The area of the triangle is", area)