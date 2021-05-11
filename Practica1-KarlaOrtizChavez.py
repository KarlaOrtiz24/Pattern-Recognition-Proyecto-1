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
def mediaBosque():
    datos = pd.read_excel(r'C:/Users/Karla/OneDrive - Instituto Politecnico Nacional/Desktop/Materias/Pattern Recognition/Proyecto1/Bosque.xlsx', sheet_name='Hoja1')
    df = pd.DataFrame(datos)

    sumar = df.loc[1,'R']
    for i in range(2, len(df)):
        total = df['R'].mean()
    print("Total", total)   
    sumarG = df.loc[1,'G']
    for i in range(2, len(df)):
        total2 = df['G'].mean()
    print("Total", total2)
    sumarB = df.loc[1,'B']
    for i in range(2, len(df)):
        total3 = df['B'].mean()
    print("Total", total3)
mediaBosque()

def mediaTierra():
    datos = pd.read_excel(r'C:/Users/Karla/OneDrive - Instituto Politecnico Nacional/Desktop/Materias/Pattern Recognition/Proyecto1/Suelo.xlsx', sheet_name='Hoja1')
    df = pd.DataFrame(datos)

    sumar = df.loc[1,'R']
    for i in range(2, len(df)):
        total = df['R'].mean()
    print("Total", total)  
    sumarG = df.loc[1,'G']
    for i in range(2, len(df)):
        total2 = df['G'].mean()
    print("Total", total2)
    sumarB = df.loc[1,'B']
    for i in range(2, len(df)):
        total3 = df['B'].mean()
    print("Total", total3)
mediaTierra()

def mediaCielo():
    datos = pd.read_excel(r'C:/Users/Karla/OneDrive - Instituto Politecnico Nacional/Desktop/Materias/Pattern Recognition/Proyecto1/Cielo.xlsx', sheet_name='Hoja1')
    df = pd.DataFrame(datos)

    sumar = df.loc[1,'R']
    for i in range(2, len(df)):
        total = df['R'].mean()
    print("Total", total)  
    sumarG = df.loc[1,'G']
    for i in range(2, len(df)):
        total2 = df['G'].mean()
    print("Total", total2)
    sumarB = df.loc[1,'B']
    for i in range(2, len(df)):
        total3 = df['B'].mean()
    print("Total", total3)
mediaCielo()
class ClasificadorBayesiano:      
        z1= [102.11, 79.13,55.81]
        z2 = [169.84,136.83,101.58]
        z3 = [201.59, 215.4, 221.64]
        A1 = np.array([[1110.74, 875.58, 743.61],[875.58,740.40,658.92],[743.61, 658.92, 629.53]])
        A2 = np.array([[1663.05, 1534.69, 1325.04], [1534.69, 1471.16, 1300.34], [1325.04, 1300.34, 1205.75]])
        A3 = np.array([[1106.44, 207.28, 2.52],[207.28, 5860.72, 4.76], [2.52, 4.76, 161.91]])
        PatronDesconocido1= [0,64,205]
        def ClasificadorGaussiano(self, pixelR, pixelG, pixelB):
                vectorPixel = np.array([pixelR,pixelG, pixelB])
                distanciaZB= vectorPixel-self.z1
                distanciaZT= vectorPixel-self.z2
                distanciaZC= vectorPixel-self.z3
                distanciaAB=self.opMatriz(distanciaZB,self.A1)
                distanciaAT=self.opMatriz(distanciaZT,self.A2)
                distanciaAC=self.opMatriz(distanciaZC,self.A3)
                distanciaB= 0
                print(distanciaAB)
                for i in distanciaAB:
                        distanciaB = distanciaB+ i**2
                distanciaB = distanciaB**0.5
                print(distanciaB)

                distanciaT=0
                for i in distanciaAT: 
                        distanciaT = distanciaT+i**2
                distanciaT = distanciaT**0.5

                distanciaC=0
                for i in distanciaAC: 
                        distanciaC = distanciaC+i**2
                distanciaC = distanciaC**0.5

                distancias = [distanciaB, distanciaT, distanciaC]
                menor = self.buscaMenor(distancias)
                print (menor)
                print (distancias)
                if menor == distanciaB: 
                        return(False, True, False) 
                if menor== distanciaT:
                        return(False, False, True)
                if menor == distanciaC: 
                        return (True, False, False)
                        
        def buscaMenor(self,distancias):
                menor=0
                for i in distancias:
                        if menor==0:
                                menor=i
                        elif menor>i:
                                menor=i
                return menor
        def opMatriz(self, distancia, covarianza):
                distanciaA=[0,0,0]
                for i in range(3):
                        for j in range(3):
                                distanciaA[i]=distanciaA[i]+(distancia[j]*covarianza[j][i])
                return (distanciaA)

                
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
                        lista = G.ClasificadorGaussiano(colorsR,colorsG,colorsB)
                        clase = ''
                        if lista[0]:
                                print('Es cielo')
                                clase= '{} es cielo'.format ([colorsR,colorsG,colorsB])
                        if lista[1]:
                                print('Es bosque')
                                clase= '{} es bosque'.format ([colorsR,colorsG,colorsB])
                        if lista[2]:
                                print('Es tierra')
                                clase = '{} es tierra'.format ([colorsR,colorsG,colorsB])
                        if cv2.waitKey(20) & 0xFF == 27:
                        
                                cv2.destroyAllWindows()
                                 

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print('Se abrio imagen')
imagen = cv2.imread(file_path)
cv2.namedWindow('imagen_CMA')
cv2.setMouseCallback('imagen_CMA', mouse)
cv2.imshow('imagen_CMA', imagen)
G = ClasificadorBayesiano()
fig=plt.figure()
ax = fig.add_subplot(projection='3d')
for m,zlow,zhigh in [('o',-50,-25), ('^', -30, -5)]:
        xs=(G.z1[0],G.z2[0],G.z3[0])
        ys= (G.z1[1], G.z2[1], G.z3[1])
        zs = (G.z1[2], G.z2[2], G.z3[2])
        ax.scatter(xs, ys,zs,marker=m)
plt.title('Clases')
plt.show()




#class Grafico: 
    #G = ClasificadorBayesiano()
    #fig=plt.figure()
    #ax = fig.add_subplot(projection='3d')
    #for m,zlow,zhigh in [('o',-50,-25), ('^', -30, -5)]:
        #xs= (G.PatronDesconocido1[0],G.PatronDesconocido1[0],G.PatronDesconocido1[0])
        #ys= (G.z1[1], G.z2[1], G.z3[1])
        #zs = (G.z1[2], G.z2[2], G.z3[2])
        #colores = ["#00cc44",  # Verde
         #  "#ff7700",  # Naranja
        #   "#ff0000"   # Rojo
       # ]
      #  ax.scatter(xs, ys,zs,marker=m, c=colores)
     #   plt.title('Clases')
    #    plt.show()

salir = False 
opcion = 0 
while not salir: 
        print("1. Opcion 1")
        print("2. Opcion 2")
        print("3. Opcion 3")
        print("4. Salir")

        print("Elige una opcion")
        if opcion == 1: 
                



