s1=10
s2=20
s3=30

valid=False

if s1+s2 > s3 and s2+s3 > s1 and s1+s3 > s2:
  valid=True

validStr="Valid" if valid else "Invalid"

print("Triangle is {}".format(validStr))