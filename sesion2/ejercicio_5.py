from math import pi, tan
s = 10
n = 5

numerator = n * pow(s, 2)
denominator = 4 * tan(pi/n)

area = numerator / denominator

print("area of polygon is: {}".format(area))