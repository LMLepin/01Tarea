import matplotlib.pyplot as plt
import numpy as np
from astropy import constants as const


infsun=np.loadtxt('sun_AM0.dat')
t,z=np.loadtxt('sun_AM0.dat', unpack=True) # Se guardan cada columna en dos arrays

alpha = len(t) - 2 # esto nos asegura  no exceder el valor de indexacion
i=0
valin1=0 #iniciamos el valor de la integral en 0

while i<=alpha:
      a=(np.fabs(t[i+1] - t[i]))*(np.fabs(z[i+1] + z[i]))/2
      valin1 += a
      i+=1

T=5778
cte=((2*np.pi*const.h)/const.c**2)*( ((const.k_B*T)/const.h)**4)
n=10000
h=((np.pi)/2 - 0)/n
a=0.0001
j=0
valin2=0
def integrando(valor):
    result=(np.tan(valor)**3)*(1 + np.tan(valor)**2)/(np.exp(np.tan(valor)) - 1)
    return result
while j<=9600:
     k= (integrando(a+(j+1)*h) + integrando(a+j*h))*h/2
     valin2+=k
     j+=1

Rsun=np.sqrt(  ((1.5*10**11)**2)*valin1/(valin2*cte))
print Rsun
