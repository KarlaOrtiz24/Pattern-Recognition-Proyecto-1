from matplotlib import pyplot as plt
from scipy import ndimage 
from skimage import io
import numpy as np
import cv2 
from PIL import Image
from skimage import io 
from random import seed
from random import randint

def extraccion(archivo):
    imagen = cv2.imread(archivo)
    h,w=20,20
    lw=[255,255,255]
    y=[]
    for i in range(h):
        for j in range(w):
            b=imagen[i,j][0]
            g=imagen[i,j][1]
            r=imagen[i,j][2]
            if r==255 and g==255 and b==255:
                y.append(1)
            else:
                y.append(0)
    return y
#Generacion de ruido aditivo, sustrativo y mixto
def generarRuido(porcentaje,tipo,y):
    yR=y
    h,w=20,20
    num=0
    #Conteo de valores blancos y negros
    for i in range(len(y)):
        #Ruido aditivo-De 0 a 1
        if tipo==1:
            if y[i]==0:
                num=num+1
        #Ruido sustrativo-De 1 a 0
        elif tipo==2:
            if y[i]==1:
                num=num+1
        #Ruido mixto
        elif tipo==3:
            num=len(y)
    print("Numero de pixeles:",num)
    num=num*porcentaje
    if num<1:
        num=1;
    print("Porcentaje: ",num)
    seed(1)
    while num>=1:
        #Ruido aditivo-De 0 a 1
        if tipo==1:
            valor=randint(0,len(y)-1)
            if(y[valor]==0):
                yR[valor]=1
                num=num-1
        #Ruido sustrativo
        elif tipo==2:
            valor=randint(0,len(y)-1)
            if(y[valor]==1):
                yR[valor]=0
                num=num-1
        #Ruido mixto
        elif tipo==3:
            valor=randint(0,len(y)-1)
            if(y[valor]==0):
                yR[valor]=1
                num=num-1
            elif(y[valor]==1):
                yR[valor]=0
                num=num-1
    res=''
    for i in range(len(yR)):
        res=res+str(yR[i])
        if (i+1)%20==0:
            res=res+'\n'
    print(res)
    return yR

print("Inicio programa")
#Vector de entrada
x1=[1,0,0,0,0]
x2=[0,1,0,0,0]
x3=[0,0,1,0,0]
x4=[0,0,0,1,0]
x5=[0,0,0,0,1]
#Vector de salida
y1=extraccion('a.bmp')
y2=extraccion('e.bmp')
y3=extraccion('i.bmp')
y4=extraccion('o.bmp')
y5=extraccion('u.bmp')
yR=generarRuido(0.01,1,y3)
while(1):
    if cv2.waitKey(0):
        cv2.destroyAllWindows()
            
