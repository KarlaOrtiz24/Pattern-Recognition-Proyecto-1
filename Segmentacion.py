from matplotlib import pyplot as plt
from scipy import ndimage 
from skimage.color import rgb2gray
from skimage import io 
import numpy as np 
import cv2 
from PIL import Image
from skimage import io 


def Mediana(nombre, valor):
    imagen = cv2.imread(r'C:\Users\sonic\Documents\ESCOM\Octavo Semestre\Pattern Recognition\Pattern-Recognition-Proyecto-1-main\Pattern-Recognition-Proyecto-1-main\CMA-x1.png', 0)
    cv2.imshow('original', imagen)
    img2 = cv2.medianBlur(imagen, valor)
    cv2.imshow("Mediana", img2)
    cv2.waitKey(0)
    cv2.imwrite (r'C:\Users\sonic\Documents\ESCOM\Octavo Semestre\Pattern Recognition\Pattern-Recognition-Proyecto-1-main\Pattern-Recognition-Proyecto-1-main\Mediana.jpg', img2)

def Minimo(n,ruta):
    img = cv2.imread(ruta)

      #Crea la forma del kernel
    tam = (n, n)
    forma = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(forma, tam)

      # Aplica el filtro minimo
    imgResult = cv2.erode(img, kernel)

      #Muestra el resultado
    cv2.namedWindow('Resultado con n ' + str(n), cv2.WINDOW_NORMAL
    cv2.imshow('Resultado con n ' + str(n), imgResult)

def Maximo(n,ruta):
    img = cv2.imread(ruta)

      # Creates the shape of the kernel
    tam = (n,n)
    forma = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(forma, tam)

      # Applies the maximum filter with kernel NxN
    imgResult = cv2.dilate(img, kernel)

      # Shows the result
    cv2.namedWindow('Result with n ' + str(n), cv2.WINDOW_NORMAL) # Adjust the window length
    cv2.imshow('Result with n ' + str(n), imgResult)

imagen = cv2.imread('CMA-x1.png')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen', gris)
cv2.waitKey(0)
cv2.imwrite('gris.jpg', gris)#para guardarla
Maximo(3,'gris.jpg')
Minimo(5,'gris.jpg')
