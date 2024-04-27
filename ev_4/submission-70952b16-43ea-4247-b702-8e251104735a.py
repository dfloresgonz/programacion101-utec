def pregunta_1(promedio: float, apellido: str) -> str:
  seccion=""
  grupo=""
  grupo1=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
  grupo2=["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  if promedio >= 17.5:
    seccion="A"
  elif promedio >= 14 and promedio < 17.5:
    seccion="B"
  elif promedio >= 11 and promedio < 14:
    seccion="C"
  else:
    seccion="D"
  if apellido[0] in grupo1:
    grupo="1"
  elif apellido[0] in grupo2:
    grupo="2"
  else:
    grupo="-"
  return "{}{}".format(seccion,grupo)

def pregunta_2(votaciones: str) -> str:
  candidate1=votaciones.count("a")
  candidate2=votaciones.count("b")
  total=len(votaciones)
  resultado="no winner"
  #print(candidate1,candidate2,total)
  if(candidate1>candidate2):
    porcentaje=(candidate1/total)*100
    #print(porcentaje,"%")
    if porcentaje > 40:
      resultado = "winner: a"
  elif(candidate2>candidate1):
    porcentaje=(candidate2/total)*100
    if porcentaje > 40:
      resultado = "winner: b"
  return resultado

def pregunta_3(nombres: list, idiomas: list, reproducciones: list) -> str:
  counter=0
  idx=0
  while idx < len(reproducciones):
    if reproducciones[idx] >= 1000000 and idiomas[idx] == 'español':
      counter+=1
    idx+=1
  return "grammy latino" if counter >=3 else "sin premio"
