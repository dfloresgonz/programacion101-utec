import math
def pregunta_1(numero: int) -> str:
  divisores = 0
  for i in range(2, numero):
    if numero % i == 0:
      divisores += 1
      break
  return "No es primo" if divisores > 0 else "Es primo"

def pregunta_2(codigo: int) -> str:
  codigos = [1,52,55,54,57,56,58,51]
  paises = ["Estados Unidos","Mexico","Brasil","Argentina","Colombia","Chile","Venezuela","Peru"]
  if codigo not in codigos:
    return "El codigo no esta registrado"
  try:
    indice=codigos.index(codigo)
    return "El pais con codigo {} es {}".format(codigo, paises[indice])
  except IndexError:
    return "El codigo no esta registrado"

def pregunta_3(segundos: int) -> str:
  CANT_SECS_HOUR=3600
  CANT_SECS_MINUTE=60
  # CANT_

  hours=segundos/CANT_SECS_HOUR

  remaining = segundos - ( math.floor(hours) * CANT_SECS_HOUR)

  minutes = remaining/CANT_SECS_MINUTE
  remaining = remaining - ( math.floor(minutes) * CANT_SECS_MINUTE)

  seconds = minutes % 1
  seconds = round(CANT_SECS_MINUTE * seconds)

  return "{} horas, {} minutos y {} segundos".format(math.floor(hours), math.floor(minutes), seconds)

def pregunta_4(numero: int) -> int:
  i = 1
  result = 1
  while i <= numero:
    result *= i
    i += 1
  return result