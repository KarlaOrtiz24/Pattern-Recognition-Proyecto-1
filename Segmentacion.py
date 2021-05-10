from matplotlib import pyplot as plt
from scipy import ndimage 
from skimage.color import rgb2gray
from skimage import io 
import numpy as np 
import cv2 
from PIL import Image
from skimage import io 

def Umbralizacion(imagen,x):
    gray = cv2.medianBlur(imagen, 5)

    _, dst1 = cv2.threshold(gray, int(x), 255, cv2.THRESH_BINARY)
#    cv2.imshow('umbral fijo', dst1)
    cv2.imwrite('umbral.jpg', dst1)#para guardarla

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
    tam = (int(n), int(n))
    forma = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(forma, tam)

      # Aplica el filtro minimo
    imgResult = cv2.erode(img, kernel)

      #Muestra el resultado
    cv2.namedWindow('Resultado con n ' + str(n), cv2.WINDOW_NORMAL)
    cv2.imshow('Resultado con n ' + str(n), imgResult)
    cv2.waitKey(50)

def Maximo(n,ruta):
    img = cv2.imread(ruta)

      # Crea la forma del kernel
    tam = (int(n),int(n))
    forma = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(forma, tam)

      #Aplica el filtro
    imgResult = cv2.dilate(img, kernel)

      #Muestra el resultado
    cv2.namedWindow('Result with n ' + str(n), cv2.WINDOW_NORMAL) 
    cv2.imshow('Result with n ' + str(n), imgResult)
    cv2.waitKey(50)

imagen = cv2.imread('CMA-x1.png')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen', gris)
cv2.waitKey(0)
cv2.imwrite('gris.jpg', gris)#para guardarla
continuar=False
while continuar==False:
    print("Inserte el valor del filtro para realizar la umbralización")
    x=input()
    Umbralizacion(gris,x)
    print("Inserte el valor para el filtro Maximo, de preferencia un número entre 1 y 10")
    n=input()
    Maximo(n,'umbral.jpg')
    print("Inserte el valor para el filtro Minimo, de preferencia un número entre 1 y 10")
    m=input()
    Minimo(m,'umbral.jpg')
    BN = cv2.imread('umbral.jpg')
    cv2.imshow('umbral fijo', BN)
    cv2.waitKey(50)
    print("Esta satisfecho con el resultado?")
    respuesta=input()
    if respuesta=="Y":
        continuar=True
    else:
        continuar=False
    
