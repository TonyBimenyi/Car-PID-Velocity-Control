import numpy as np
import matplotlib.pyplot as plt

# DEFINE MODEL

def vehicule(v,t,u,load):
    # inputs
    # v   = vehicule velocity(m/s)
    # t= time (sec)
    # u= gas pedal position (-50% to 100%)
    # load = passenger load + cargo (kg)
    Cd = 0.24   #drag coefficient
    rho = 1.225 #air density (kg/m^3)
    A = 5.0     #cross sectionnal area (m^2)
    Fp = 50    #thrust parameter (N/%pedal)
    m = 500     #vehicule mass(Kg)

    # CALCULATE DERIVATIVE EF VELOCITY
    dv_dt = (1.0/(m+load)) * (Fp*u - 0.5*rho*Cd*A*v^2)
    