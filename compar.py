''' Este codigo tiene por objetivo comparar los algoritmos obtenidos
mediante dos rutinas predefinidas scipy.quad y scipy.trapz '''
from scipy import integrate
import numpy as np
from astropy import constants as const


########### Comparacion integral 1 ############################################
infsun=np.loadtxt('sun_AM0.dat')
t,z=np.loadtxt("sun_AM0.dat", unpack=True) # Se guardan cada columna en dos arrays

val_scipy1=integrate.trapz(z,t) # valor obtenido con rutina de libreria

alpha= len(t) - 2 # esto nos asegura  no exceder el valor de indexacion
i=0
valin1=0 #iniciamos el valor de la integral en 0

while i<=alpha:
    a=(np.fabs(t[i+1] - t[i]))*(np.fabs(z[i+1] + z[i]))/2
    valin1 += a
    i+=1

print np.fabs( valin1 - val_scipy1) #Mostrando comparacion

##################Comparacion integral 2########################################

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


func_integ= lambda x: (x**3)/(np.exp(x) -1)
val_scipy2=integrate.quad(func_integ,0,np.inf)

print np.fabs(valin2 - val_scipy2[0]) #Mostrando comparacion
