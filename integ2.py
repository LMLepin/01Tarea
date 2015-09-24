''' Codigo para integrar numericamente la funcion de Planck mediante
la regla trapezoidal previo arreglo del dominio de integracion'''
import numpy as np
from astropy import constants as const

T=5778
cte=((2*np.pi*const.h)/const.c**2)*( ((const.k_B*T)/const.h)**4)
n=10000
h=((np.pi)/2 - 0)/n
a=0.0001
i=0
valin=0
def integrando(valor):
    result=(np.tan(valor)**3)*(1 + np.tan(valor)**2)/(np.exp(np.tan(valor)) - 1)
    return result
while i<=9600:
     k= (integrando(a+(i+1)*h) + integrando(a+i*h))*h/2
     valin+=k
     i+=1

print valin*cte
