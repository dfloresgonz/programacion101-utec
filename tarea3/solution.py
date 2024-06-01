import numpy as np

def pregunta_1(image):
  c_image = [[column[:] for column in row] for row in image]
  np_image = np.array(c_image, dtype=np.uint8)
  c = np.where(np_image * 1.6 > 255, 255, np_image * 1.6)
  c = c.round()
  return c

def pregunta_2(image):
  c_image = [ [column[:] for column in row] for row in image]
  c_image = np.array(c_image)
  reverse = c_image[:,::-1,:]
  reverse[:,:,0] = 0
  reverse[:,:,2] = 0
  return reverse

def pregunta_3(image):
  c_image = [[column[:] for column in row] for row in image]
  c_image = np.array(c_image)

  ori_red = c_image[:,:,0]
  ori_gre = c_image[:,:,1]
  ori_blu = c_image[:,:,2]

  sep_red = (0.393 * ori_red) + (0.769 * ori_gre) + (0.189 * ori_blu)
  sep_red = np.where(sep_red > 255, 255, sep_red)
  sep_red = sep_red.round()

  sep_gre = 0.349 * ori_red + 0.686 * ori_gre + 0.168 * ori_blu
  sep_gre = np.where(sep_gre > 255, 255, sep_gre)
  sep_gre = sep_gre.round()

  sep_blu = 0.272 * ori_red + 0.534 * ori_gre + 0.131 * ori_blu
  sep_blu = np.where(sep_blu > 255, 255, sep_blu)
  sep_blu = sep_blu.round()
  #
  c_image[:,:,0] = sep_red
  c_image[:,:,1] = sep_gre
  c_image[:,:,2] = sep_blu
  return c_image

def calcular(i, j, h, cx, cy):
  return (((j-cx) ** 2) + ((i-cy) ** 2)) < ((int(h/2)) ** 2)

def pregunta_4(image):
  c_image = [[column[:] for column in row] for row in image]
  h = len(c_image)
  w = len(c_image[0])
  cx = int(w / 2)
  cy = int(h / 2)

  for i in range(h):
    for j in range(w):
      c_image[i][j] = c_image[i][j] if calcular(i, j, h, cx, cy) else [0, 0, 0]
  return c_image