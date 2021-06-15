#author Karla Ortiz Chávez 
#author Rafael Rojas Fernandez 
#Pattern Recognition 3CM11
#date 04/05/2021
import numpy as np 
import cv2 
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import filedialog
import matplotlib.cm as cm 
import xlrd
def valoresR():
    arrR=[]
    datos = pd.read_excel('Bosque.xlsx', sheet_name='Hoja1')
    df = pd.DataFrame(datos)

    #sumar = df.loc[1,'R']
    for i in range(0, len(df)):
        valor = df.loc[i,'R']
        arrR.append(valor)
    datos2 = pd.read_excel('Cielo.xlsx', sheet_name='Hoja1')
    df2 = pd.DataFrame(datos2)
    for i in range(0, len(df2)):
        valor = df2.loc[i,'R']
        arrR.append(valor)
    print("Tamaño ", len(arrR))
    return arrR

def valoresG():
    arrG=[]
    datos = pd.read_excel('Bosque.xlsx', sheet_name='Hoja1')
    df = pd.DataFrame(datos)


    for i in range(0, len(df)):
        valor = df.loc[i,'G']
        arrG.append(valor)
    datos = pd.read_excel('Cielo.xlsx', sheet_name='Hoja1')
    df = pd.DataFrame(datos)
    for i in range(0, len(df)):
        valor = df.loc[i,'G']
        arrG.append(valor)
    print("Tamaño ", len(arrG))
    return arrG

def valoresB():
    arrB=[]
    arrV=[]
    datos = pd.read_excel('Bosque.xlsx', sheet_name='Hoja1')
    df = pd.DataFrame(datos)
    for i in range(0, len(df)):
        valor = df.loc[i,'B']
        arrB.append(valor)
        arrV.append(1.0)
    datos = pd.read_excel('Cielo.xlsx', sheet_name='Hoja1')
    df = pd.DataFrame(datos)
    for i in range(0, len(df)):
        valor = df.loc[i,'B']
        arrB.append(valor)
        arrV.append(-1.0)
    print("Tamaño ", len(arrB))
    return arrB,arrV

def entrenamiento(w1,w2,w3,R,G,B,epsilon,error,V,tam):
    errores=True
    while errores:
        errores=False
        for i in range (tam):
            y=((R[i]*w1)+(G[i]*w2)+(B[i]*w3)) 
            if y>0:
                y=1.0
            else:
                y=-1.0
            if y!=V[i]:
                errores=True
                error=V[i]-y
                w1=w1+(epsilon*error*R[i])
                w2=w2+(epsilon*error*G[i])
                w3=w3+(epsilon*error*B[i])
    return w1,w2,w3

class RedNeurona:
        def __init__(self,w1,w2,w3):
            self.P1 = w1
            self.P2 = w2
            self.P3 = w3
            PatronDesconocido1= [0,64,205]
        def Perceptron(self, pixelR, pixelG, pixelB):
                res=(self.P1*pixelR)+(self.P2*pixelG)+(self.P3*pixelB)
                if res>0:
                    return(True, False) 
                else:
                    return(False,True)

                
def mouse(event, x,y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                        colorsB =imagen[y,x,0]
                        colorsG=imagen[y,x,1]
                        colorsR=imagen[y,x,2]
                        colors=imagen[y,x]
                        print("Red: ",colorsR)
                        print("Green: ",colorsG)
                        print("Blue: ",colorsB)
                        colores=[colorsR,colorsG,colorsB]
                        lista = G.Perceptron(colorsR,colorsG,colorsB)
                        clase = ''
                        if lista[0]:
                                print('Es bosque')
                                clase= '{} es bosque'.format ([colorsR,colorsG,colorsB])
                        if lista[1]:
                                print('Es cielo')
                                clase= '{} es cielo'.format ([colorsR,colorsG,colorsB])
                        if cv2.waitKey(20) & 0xFF == 27:
                                cv2.destroyAllWindows()
                                 
arregloR=valoresR()
arregloG=valoresG()
arregloB,arregloV=valoresB()

w1=0.0
w2=0.0
w3=0.0
eps=0.0001
error=0.0
w1,w2,w3=entrenamiento(w1,w2,w3,arregloR,arregloG,arregloB,eps,error,arregloV,len(arregloR))
print("Peso 1: ",w1)
print("Peso 2: ",w2)
print("Peso 3: ",w3)
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print('Se abrio imagen')
imagen = cv2.imread(file_path)
cv2.namedWindow('imagen_CMA')
cv2.setMouseCallback('imagen_CMA', mouse)
cv2.imshow('imagen_CMA', imagen)
G = RedNeurona(w1,w2,w3)
plt.title('Clases')
plt.show()
