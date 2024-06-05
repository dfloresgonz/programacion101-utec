import numpy as np

def readfile(filename):
  with open(filename, 'r') as entradaf:
    contenido = entradaf.read()
    data = contenido.split('\n')
    entradaf.close()
    data = [n.split(' ') for n in data]
    data.pop()
    return data

def pregunta1():
  numeros = readfile('sequences.in')
  for n in numeros:
    arr = np.array(n, dtype=np.uint8)

    idx1=(arr[len(arr) - 2])
    idx2=(arr[len(arr) - 1])+1

    sum = np.sum(arr[idx1:idx2])

    print('The sum of elements from index {} to {} is {}'.format(idx1, idx2-1, sum))
  return

def pregunta2():
  palabras = readfile('words.in')
  for index, palabra in enumerate(palabras):
    dictionary = {}
    for w in palabra:
      if dictionary.get(w) != None:
        dictionary[w] += 1
      else:
        dictionary[w] = 1
    print('Pharse {}'.format(index+1))
    for k in dictionary:
      print('The word {} appears {} times.'.format(k, dictionary[k]))
  return

def pregunta3():
  numeros = readfile('temperatures.in')
  for num in numeros:
    arr = np.array(num, dtype=np.float64)

    idx1 = int(arr[len(arr) - 2])
    idx2 = int(arr[len(arr) - 1])

    avg = np.average(arr[idx1:idx2+1])
    avg = round(avg, 2)

    print('The average temperature from day {} to day {} is {}'.format(idx1, idx2, avg))
  return

def pregunta4():
  numeros = readfile('sales.in')
  for num in numeros:
    arr = np.array(num, dtype=np.float64)

    threshold = arr[-1]
    highest = np.argmax(arr)
    lowest = np.argmin(arr)
    total = np.sum(arr)
    greater_than_threshold = np.where(arr > threshold)

    print('Highest sales on day {}'.format(highest))
    print('Lowest sales on day {}'.format(lowest))
    print('Total sales: {}'.format(total))
    print('Days with sales above threshold: {}'.format(greater_than_threshold))
  return