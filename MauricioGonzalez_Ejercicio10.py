import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal
datos=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt',sep=";",header=None, decimal=",")
datos[0]=pd.to_datetime(datos[0],format='%d/%m/%Y %H:%M:%S')
#datos.set_index([0],inplace=True)
datos[1]=pd.to_datetime(datos[1],format='%d/%m/%Y %H:%M:%S')
#datos.set_index([1],inplace=True)
datos[1]=str(datos[1])
datos[1]=datos[1].str[1:20]
datos2=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt',sep=";",header=None, decimal=",")
datos2[0]=pd.to_datetime(datos2[0],format='%d/%m/%Y %H:%M:%S')
#datos.set_index([0],inplace=True)
datos2[1]=pd.to_datetime(datos2[1],format='%d/%m/%Y %H:%M:%S')
#datos.set_index([1],inplace=True)
datos2[1]=str(datos2[1])
datos2[1]=datos2[1].str[1:20]
datos3=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2010.txt',sep=";",header=None, decimal=",")
datos3[0]=pd.to_datetime(datos3[0],format='%d/%m/%Y %H:%M:%S')
#datos.set_index([0],inplace=True)
datos3[1]=pd.to_datetime(datos3[1],format='%d/%m/%Y %H:%M:%S')
#datos.set_index([1],inplace=True)
datos3[1]=str(datos3[1])
datos3[1]=datos3[1].str[1:20]
plt.figure(figsize=(12,12))
plt.subplot(2,2,1)
plt.plot(datos[0],datos[2])
plt.subplot(2,2,2)
plt.plot(datos2[0],datos2[2])
plt.subplot(2,2,3)
plt.plot(datos3[0],datos3[2])
N  = 2    # Orden del filtro
Wn = 0.01 # Corte de frecuancia
B, A = signal.butter(N, Wn)

cost=pd.concat([datos[2],datos2[2],datos3[2]])
cost=np.array(cost)
cost=cost.astype(np.float)
CostFil=signal.filtfilt(B,A, cost)
date=pd.concat([datos[0],datos2[0],datos3[0]])

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(date,cost, 'b-')
plt.plot(date,CostFil, 'r-',linewidth=2)
plt.ylabel(r"Costo ($^{\circ}C$)")
plt.legend(['Original','Filtrado'])
plt.title("Costos en la bolsa de valores")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(date,cost-CostFil, 'b-')
plt.ylabel(r"Costo ($^{\circ}C$)")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.savefig("FiltroCostos.png")
plt.show()