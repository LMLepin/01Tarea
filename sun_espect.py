#! /usr/bin/env python
#codigo para leer los datos y plotear.
import matplotlib.pyplot as plt
import numpy as np

infsun=np.loadtxt('sun_AM0.dat')
t,z=np.loadtxt("sun_AM0.dat", unpack=True) # Se guardan cada columna en dos arrays
a=(10)*t # Se reescala a CGS
b=(10**10)*z # se reescala a Angstrom
plt.figure(1)
plt.clf()
plt.plot (a,b)
plt.xlim(0,20000)   # Fija limites en el eje x para una mejor imagen
plt.title('Espectro del Sol ( Flujo vs Longitud de onda)')
plt.xlabel('Longitud de onda [$\AA$]')
plt.ylabel('Flujo en [$erg/(s cm^{2} cm)$]')
plt.savefig('Espectro.png')
plt.show()
