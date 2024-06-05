import numpy as np
def pregunta1():
  archivo_entrada='sequences.in'
  with open(archivo_entrada, 'r') as entradaf:
    contenido = entradaf.read()
    numeros = contenido.split('\n')
    for n in numeros:
      num = n.split(' ')
      if num[0] != '-1':
        arr = np.array(num, dtype=np.uint8)
        idx1=(arr[len(arr) - 2])
        idx2=(arr[len(arr) - 1])+1
        sum = np.sum(arr[idx1:idx2])
        print('The sum of elements from index {} to {} is {}'.format(idx1, idx2-1, sum))
        pass
    entradaf.close()
  return

def pregunta2():
  archivo_entrada='words.in'
  idx=1
  with open(archivo_entrada, 'r') as entradaf:
    contenido = entradaf.read()
    palabras = contenido.split('\n')
    for p in palabras:
      palabra = p.split(' ')
      if palabra[0] != 'END':
        dictionary = {}
        for w in palabra:
          if dictionary.get(w) != None:
            dictionary[w] += 1
          else:
            dictionary[w] = 1
        print('Pharse {}'.format(idx))
        for k in dictionary:
          print('The word {} appears {} times.'.format(k, dictionary[k]))
      idx+=1
    entradaf.close()
  return


def pregunta3():
  archivo_entrada = 'temperatures.in'
  with open(archivo_entrada, 'r') as entradaf:
    contenido = entradaf.read()
    numeros = contenido.split('\n')
    for n in numeros:
      num = n.split(' ')
      if num[0] != '-1':
        arr = np.array(num, dtype=np.float64)
        # print(arr)
        idx1 = int(arr[len(arr) - 2])
        idx2 = int(arr[len(arr) - 1]) + 1
        avg = np.average(arr[idx1:idx2])
        avg = round(avg, 2)
        print('The average temperature from day {} to day {} is {}'.format(idx1, idx2-1, avg))
        pass
    entradaf.close()
  return

def pregunta4():
  archivo_entrada = 'sales.in'
  with open(archivo_entrada, 'r') as entradaf:
    contenido = entradaf.read()
    numeros = contenido.split('\n')
    for n in numeros:
      num = n.split(' ')
      if num[0] != '-1':
        arr = np.array(num, dtype=np.float64)
        threshold = arr[-1]
        highest = np.argmax(arr)
        lowest = np.argmin(arr)
        total = np.sum(arr)
        greaten_than_threshold = np.where(arr > threshold)
        print('Highest sales on day {}'.format(highest))
        print('Lowest sales on day {}'.format(lowest))
        print('Total sales: {}'.format(total))
        print('Days with sales above threshold: {}'.format(greaten_than_threshold))
        pass
    entradaf.close()