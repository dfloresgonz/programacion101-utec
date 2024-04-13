num1=12
num2=99
num3=12

min_num=min(num1,num2,num3)
max_num=max(num1,num2,num3)

middle=0
if min_num==num1 and max_num==num2:
  middle=num3
elif min_num==num3 and max_num==num1:
  middle=num2
else:
  middle=num1

print("{}, {}, {}".format(min_num,middle,max_num))