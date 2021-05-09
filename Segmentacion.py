from matplotlib import pyplot as plt
from scipy import ndimage 
from skimage.color import rgb2gray
from skimage import io 
import numpy as np 
import cv2 
from PIL import Image
from skimage import io 

imagen = cv2.imread(r'C:\Users\Karla\OneDrive - Instituto Politecnico Nacional\Desktop\Materias\Pattern Recognition\Proyecto1\CMA-x1.png')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen', gris)
cv2.waitKey(0)
cv2.imwrite(r'C:\Users\Karla\OneDrive - Instituto Politecnico Nacional\Desktop\Materias\Pattern Recognition\Proyecto1\gris.jpg', gris)#para guardarla

def Mediana(nombre, valor):
    imagen = cv2.imread(r'C:\Users\Karla\OneDrive - Instituto Politecnico Nacional\Desktop\Materias\Pattern Recognition\Proyecto1\CMA-x1.png', 0)
    cv2.imshow('original', imagen)
    img2 = cv2.medianBlur(imagen, valor)
    cv2.imshow("Mediana", img2)
    cv2.waitKey(0)
    cv2.imwrite (r'C:\Users\Karla\OneDrive - Instituto Politecnico Nacional\Desktop\Materias\Pattern Recognition\Proyecto1\Mediana.jpg', img2)

def Minimo(nombre):
    imagen = Image.open(r'C:\Users\Karla\OneDrive - Instituto Politecnico Nacional\Desktop\Materias\Pattern Recognition\Proyecto1\Mediana.jpg')
    imagen.show()
    Histograma(img)

    copia = Image.new('RGB', img.size)
    datosImg = Image.Image.getdata(imagen)
    copia.putdata(datosImg)
    ancho, alto = img.size

    for i in range(ancho):
        for j in range(alto):
            r, g, b = copia.getpixel((i,j))
            x = (r + g + b) / 3
            intx = int (x)
            pixel = tuple ([intx, intx, intx])
            copia.putpixel((i,j), pixel)

    for i in range(ancho):
        for j in range(alto):
            vecindades = ObtenerVecinos(img, i, j)
            mini = min(((vecindades[0][0]), (vecindades[1][0]), (vecindades[2][0]), 
                        (vecindades[3][0]), (vecindades[4][0]), (vecindades[5][0]), 
                        (vecindades[6][0]), (vecindades[7][0]), (vecindades[8][0])))
            res = mini
            pixel = tuple([res, res, res])
            copia.putpixel((i, j), pixel)

    copia.show()
    copia.save(r'C:\Users\Karla\OneDrive - Instituto Politecnico Nacional\Desktop\Materias\Pattern Recognition\Proyecto1\Min.jpg')
    Histograma(copia)


