
def pregunta_1(dia : int, mes: int) ->str:
  estacion = ""
  if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
    estacion = "Verano"
  elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 21):
    estacion = "Otonno"
  elif (mes == 6 and dia >= 22) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 22):
    estacion = "Invierno"
  else:
    estacion = "Primavera"
  return estacion

def pregunta_2(n1 :  int, n2: int) ->int:
  response = 0
  for i in range(n1, n2+1):
    if (i % 35 == 0) or (i % 12 == 0):
      response += i
  return response

def pregunta_3(numero : int)-> int:
  response = 0
  for i in range(numero):
    if (i > 0 and numero % i == 0):
      response += i
  return response

def pregunta_4(numeroDeTerminos :  int) -> int:
  response = 0
  for i in range(numeroDeTerminos+1):
    response += pow(i, 3)
  return response