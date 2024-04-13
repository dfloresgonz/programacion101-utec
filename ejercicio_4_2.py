import math

CANT_SECS_DAY=86400
CANT_SECS_HOUR=3600
CANT_SECS_MINUTE=60

seconds=int(input("seconds: "))

days=seconds/CANT_SECS_DAY

remaining = seconds - ( math.floor(days) * CANT_SECS_DAY)
hours = remaining/CANT_SECS_HOUR

remaining = remaining - ( math.floor(hours) * CANT_SECS_HOUR)

minutes = remaining/CANT_SECS_MINUTE
remaining = remaining - ( math.floor(minutes) * CANT_SECS_MINUTE)

seconds = minutes % 1
seconds = round(CANT_SECS_MINUTE * seconds)

print("{}:{}:{}:{}".format(math.floor(days), math.floor(hours), math.floor(minutes), seconds))