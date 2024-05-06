import datetime

def pregunta_1(inicio: int, ultimo: int, divisor: int = 7) -> float:
  multiplos = []
  avg = 0
  for i in range(inicio, ultimo + 1):
    if i % divisor == 0:
      multiplos.append(i)
  if len(multiplos) > 0:
    avg = sum(multiplos) / len(multiplos)
  return avg

def pregunta_2(fecha: str) -> int:
  hoy = datetime.date.today()
  fech = datetime.datetime.strptime(fecha, '%Y-%m-%d').date()
  diff = (fech - hoy)
  diff = abs(diff.days)
  return diff

def pregunta_3(lista: list, minimo: float) -> bool:
  response = False
  if len(lista) == 0:
    return False
  for i in lista:
    if not isinstance(i, (int, float)):
      raise TypeError('LA LISTA DEBE CONTENER SOLO NUMEROS')
    if i <= minimo:
      raise ValueError('NO TODOS LOS NUMEROS SON MAYORES QUE EL VALOR MINIMO')
    response = True
  return response


def pregunta_4(archivo_entrada: str, archivo_salida: str) -> float | None:
  def es_primo(numero: int) -> bool:
    divisores = 0
    for i in range(2, numero):
      if numero % i == 0:
        divisores += 1
        break
    return False if divisores > 0 else True

  # Tu codigo aqui
  suma = 0
  primos = []
  try:
    with open(archivo_entrada, 'r') as entradaf:
      contenido = entradaf.read()
      numeros = contenido.split('\n')
      numeros = [int(num) for num in numeros[0:-1]]
      suma = sum(numeros)
      for i in range(2, suma + 1):
        if es_primo(i):
          primos.append(str(i)+'\n')
      entradaf.close()
  except FileNotFoundError:
    return None
  finally:
    with open(archivo_salida, 'w') as salida:
      salida.writelines(primos)
      salida.close()
  return suma