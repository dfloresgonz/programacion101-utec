min_range = 50
MAX_RANGE = 555
response = []

while min_range <= MAX_RANGE:
  multiplo = min_range % 5
  if multiplo == 0:
    response.append(min_range)
  min_range = min_range + 5

print(response)
