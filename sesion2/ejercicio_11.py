number=8912 # change here <<<

first=number//1000
rest=number % 1000

second=rest//100
rest=rest % 100

third=rest//10
rest=rest % 10

fourth=rest

sum = first+second+third+fourth

print("The sum of {}{}{}{} is: {}".format(first,second,third,fourth,sum))