import numpy as np
import cv2

def convolucion(I_original, Kernel):
    fr = len(I_original)-len(Kernel)+ 1
    cr = len(I_original[0])-len(Kernel[0])+1
    Resultado = np.zeros((fr,cr), np.uint8)
    #For para recorrer  filas
    for i in range(len(Resultado)):
        #For para recorrer columnas
        for j in range(len(Resultado[0])):
            suma= 0
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                    suma+=Kernel[m][n] * I_original[m+i][n+j]
            if suma<=255:
                Resultado[i][j]=round(suma)
            else:
                Resultado[i][j]=255
    return Resultado

#Imagenes 
K = [[-1,0,1],[-1,0,1],[-1,0,1]]
I = [[2,0,1,1,2],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]

#imagenes a numpy arrays
In = np.array(I)
Kn = np.array(K)
IRGB = cv2.imread('MasterYoda2.jpg')
IGS = cv2.cvtColor(IRGB, cv2.COLOR_BGR2GRAY)
print(IGS.shape)

#Función de convolución
R = convolucion(IGS,Kn)
print(R.shape)
print(R)
cv2.imwrite('MasterYodaC.jpg', R)
