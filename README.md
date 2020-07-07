# Tarea4
Solucion a la Tarea 4 del curso Modelos Probabilisticos de Senales y Sistemas

Para la primera parte, se crea una onda sinuoidal de amplitud igual a 1s.
Con esta onda se modula de forma BPSK, de forma que cuando en los bits haya 
un 1 se tendra una onda sinoidal positiva, y cuando haya un bit igual a 0
habra una onda sinoidal pero positiva. Estas imagenes se muestran en las figuras
"portadora" y "senalmodulada" respectivamente.

Para la segunda parte se calculo la potencia promedio de la senal la cual dio
un valor de 0.4900009800019598 W.

Para la tercera parte se simulo un canal ruidoso, para un SNR en el rango de -2dB a 3dB.
Esto nos genero 6 valores de sigma, los cuales se utilizaron para generar 6 canales
ruidosos (uno para cada valor dentro del rango del SNR). Posterior a esto, se genero
una senal de ruido la cual se sumo a la senal portadora para simular el paso de la
senal portadora ante los 6 diferentes canales ruidosos. Estos se muestran en las figuras
"rx1", "rx2", ... , "rx6"

Para la cuarta parte se simulo una grafica de la densidad espectral con el comando 
"welch" de python, para antes y despues de pasar por el canal ruidoso. Las graficas 
obtenidas se muestran en las figuras "deantes" y "dedespues".

Para la quinta y ultima parte, se simulo el BER vs el SNR. Para esto, de los resultados
obtenidos en la tercera parte se generaron dos vectores de 6 espacios cada uno. Uno para
el SNR [-2dB, -1dB, .... , 3dB] y otro para el BER obtenido de cada Rxn. La grafica se 
muestra en la figura "snrvsber".
