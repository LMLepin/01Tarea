from scipy import integrate
import numpy as np
from astropy import constants as const

def integracion():
  func_integ= lambda x: (x**3)/(np.exp(x) -1)
  val_scipy2=integrate.quad(func_integ,0,np.inf)
  return val_scipy2
  
