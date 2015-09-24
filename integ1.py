''' Codigo para integrar numericamente el espectro del sol mediante
la regla trapezoidal sin paso constante '''
import matplotlib.pyplot as plt
import numpy as np



infsun=np.loadtxt('sun_AM0.dat')
t,z=np.loadtxt('sun_AM0.dat', unpack=True) # Se guardan cada columna en dos arrays

n = len(t) - 2 # esto nos asegura  no exceder el valor de indexacion
i=0
valin=0 #iniciamos el valor de la integral en 0

while i<=n:
      a=(np.fabs(t[i+1] - t[i]))*(np.fabs(z[i+1] + z[i]))/2
      valin += a
      i+=1

print valin 
