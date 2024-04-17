grade1=float(input("Type the first grade: "))
grade2=float(input("Type the second grade: "))
grade3=float(input("Type the third grade: "))

result = (grade1 * 0.30) + (grade2 * 0.30) + (grade3 * 0.40)

result = round(result, 2)

print("The weighted average is " + str(result))