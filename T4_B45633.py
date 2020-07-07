#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate
import pandas as pd
import matplotlib.pyplot as plt
bits = []
with open ('C:\\Users\\fabir\\Desktop\\Modelos\\bits10k.csv', 'r') as X:
    lines = X.read().splitlines()
    for row in lines:
        bits.append(float(row))


# In[2]:


# Modulacion de la senal - Parte 1
# Numero de bits
N = len(bits)
print('El numero de bits es:' ,N)
# Frecuencia de operacion 
f = 5000 #Hz
# Duracion del periodo de cada simbolo
T = 1/f #s
# Numero de puntos de muestreo por periodo
p = 50
# Puntos de muestreo para cada periodo
tp = np.linspace(0, T, p)
# Creacion de la forma de onda de la portadora
sinus = np.sin(2*np.pi*f*tp)
# Visualizacion de la forma de onda de la portadora
plt.plot(tp, sinus)
plt.xlabel('Tiempo [s]')
plt.ylabel('Portadora')
# Frecuencia de muestreo
fs = p/T
print('La frecuencia de muestreo es:' ,fs) #250k Hz
# Creacion de la linea temporal para todo el Tx 
t = np.linspace(0, N*T, N*p)
# Inicializar el vector de la senal
senal = np.zeros(t.shape)


# In[3]:


# Creacion de la senal modulada
for k, b in enumerate(bits):
    if b == 1:
        senal[k*p:(k+1)*p] = b*sinus
    else:
        senal[k*p:(k+1)*p] = -sinus
        
# Visualisacion de los primeros bits modulados
pb = 5
plt.figure()
plt.plot(senal[0:pb*p])
plt.ylabel('Tx')   


# In[4]:


# Calculo de la potencia promedio - Parte 2
Pinst = senal**2
Ps = integrate.trapz(Pinst ,t) / (N * T)
print('La potencia promedio es:', Ps)
# Relacion senal a ruido deseada
SNR = np.linspace(-2, 3, 6)
Pn = Ps / (10**(SNR/10))
sigma = np.sqrt(Pn)
print(sigma)


# In[5]:


# Simulacion de canal ruidoso tipo AWGN - Parte 3
# Creacion de ruido
ruido0  = np.random.normal(0, sigma[0], senal.shape)
# Simular el canal: senal recibida
Rx0 = senal + ruido0
pb = 5
plt.figure()
plt.plot(Rx0[0:pb*p])
plt.ylabel('Rx0')
plt.title('Rx0 para SNR = -2dB')

# Demodular y decodificar la senal - Parte 5
# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(sinus**2)
# Inicializacion del vector de bits recibidos
bitsRx0 = np.zeros(N)
# Decodificacion de la senal por deteccion de energia
for k, b in enumerate(bits):
    Ep = np.sum(Rx0[k*p:(k+1)*p]*sinus) 
    if Ep > Es/2:
        bitsRx0[k] = 1
    else:
        bitsRx0[k] = 0
    err0 = np.sum(np.abs(bits - bitsRx0))
    BER0 = 100*(err0/N)
print('Para un SNR de -2dB hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err0, N, BER0))


# In[6]:


# Simulacion de canal ruidoso tipo AWGN - Parte 3
# Creacion de ruido
ruido1  = np.random.normal(0, sigma[1], senal.shape)
# Simular el canal: senal recibida
Rx1 = senal + ruido1
pb = 5
plt.figure()
plt.plot(Rx1[0:pb*p])
plt.ylabel('Rx1')
plt.title('Rx1 para SNR = -1dB')

# Demodular y decodificar la senal - Parte 5
# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(sinus**2)
# Inicializacion del vector de bits recibidos
bitsRx1 = np.zeros(N)
# Decodificacion de la senal por deteccion de energia
for k, b in enumerate(bits):
    Ep = np.sum(Rx1[k*p:(k+1)*p]*sinus) 
    if Ep > Es/2:
        bitsRx1[k] = 1
    else:
        bitsRx1[k] = 0
    err1 = np.sum(np.abs(bits - bitsRx1))
    BER1 = 100*(err1/N)
print('Para un SNR de -1dB hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err1, N, BER1))


# In[7]:


# Simulacion de canal ruidoso tipo AWGN - Parte 3
# Creacion de ruido
ruido2  = np.random.normal(0, sigma[2], senal.shape)
# Simular el canal: senal recibida
Rx2 = senal + ruido2
pb = 5
plt.figure()
plt.plot(Rx2[0:pb*p])
plt.ylabel('Rx2')
plt.title('Rx2 para SNR = 0dB')

# Demodular y decodificar la senal - Parte 5
# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(sinus**2)
# Inicializacion del vector de bits recibidos
bitsRx2 = np.zeros(N)
# Decodificacion de la senal por deteccion de energia
for k, b in enumerate(bits):
    Ep = np.sum(Rx2[k*p:(k+1)*p]*sinus) 
    if Ep > Es/2:
        bitsRx2[k] = 1
    else:
        bitsRx2[k] = 0
    err2 = np.sum(np.abs(bits - bitsRx2))
    BER2 = 100*(err2/N)
print('Para un SNR de 0dB hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err2, N, BER2))


# In[8]:


# Simulacion de canal ruidoso tipo AWGN - Parte 3
# Creacion de ruido
ruido3  = np.random.normal(0, sigma[3], senal.shape)
# Simular el canal: senal recibida
Rx3 = senal + ruido3
pb = 5
plt.figure()
plt.plot(Rx3[0:pb*p])
plt.ylabel('Rx3')
plt.title('Rx3 para SNR = 1dB')

# Demodular y decodificar la senal - Parte 5
# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(sinus**2)
# Inicializacion del vector de bits recibidos
bitsRx3 = np.zeros(N)
# Decodificacion de la senal por deteccion de energia
for k, b in enumerate(bits):
    Ep = np.sum(Rx3[k*p:(k+1)*p]*sinus) 
    if Ep > Es/2:
        bitsRx3[k] = 1
    else:
        bitsRx3[k] = 0
    err3 = np.sum(np.abs(bits - bitsRx3))
    BER3 = 100*(err3/N)
print('Para un SNR de 1dB hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err3, N, BER3))


# In[9]:


# Simulacion de canal ruidoso tipo AWGN - Parte 3
# Creacion de ruido
ruido4  = np.random.normal(0, sigma[4], senal.shape)
# Simular el canal: senal recibida
Rx4 = senal + ruido4
pb = 5
plt.figure()
plt.plot(Rx4[0:pb*p])
plt.ylabel('Rx4')
plt.title('Rx4 para SNR = 2dB')

# Demodular y decodificar la senal - Parte 5
# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(sinus**2)
# Inicializacion del vector de bits recibidos
bitsRx4 = np.zeros(N)
# Decodificacion de la senal por deteccion de energia
for k, b in enumerate(bits):
    Ep = np.sum(Rx4[k*p:(k+1)*p]*sinus) 
    if Ep > Es/2:
        bitsRx4[k] = 1
    else:
        bitsRx4[k] = 0
    err4 = np.sum(np.abs(bits - bitsRx4))
    BER4 = 100*(err4/N)
print('Para un SNR de 2dB hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err4, N, BER4))


# In[10]:


# Simulacion de canal ruidoso tipo AWGN - Parte 3
# Creacion de ruido
ruido5  = np.random.normal(0, sigma[5], senal.shape)
# Simular el canal: senal recibida
Rx5 = senal + ruido5
pb = 5
plt.figure()
plt.plot(Rx5[0:pb*p])
plt.ylabel('Rx5')
plt.title('Rx5 para SNR = 3dB')

# Demodular y decodificar la senal - Parte 5
# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(sinus**2)
# Inicializacion del vector de bits recibidos
bitsRx5 = np.zeros(N)
# Decodificacion de la senal por deteccion de energia
for k, b in enumerate(bits):
    Ep = np.sum(Rx5[k*p:(k+1)*p]*sinus) 
    if Ep > Es/2:
        bitsRx5[k] = 1
    else:
        bitsRx5[k] = 0
    err5 = np.sum(np.abs(bits - bitsRx5))
    BER5 = 100*(err5/N)
print('Para un SNR de 3dB hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err5, N, BER5))


# In[12]:


# Densidad espectral de potencia de la senal antes y despues del canal ruidoso - Parte 4
# Antes del canal ruidoso
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.show()

# Después del canal ruidoso
fw, PSD = signal.welch(Rx1, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.show()


# In[16]:


#Grafica de BER vs SNR
BER = np.array([BER0, BER1, BER2, BER3, BER4, BER5])
plt.figure()
plt.plot(BER, SNR)
plt.ylabel('SNR [dB]')
plt.xlabel('BER')
plt.show()

