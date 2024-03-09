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
    return dv_dt


tf = 60.0                   # final time for simulation
nsteps = 61                 # number of time steps
delta_t = tf/(nsteps-1)     # how long is each time step?
ts = np.linspace(0,tf,nsteps)   # linearly spaced time vector

#Simulate step test operation
step = np.zeros(nsteps) # u = valve % open
step[11:] = 50.0    #step up pedal
#passengers + cargo load
load = 200.0 # Kg
#velocity initial condition
v0 = 0.0
#for storing the results
vs = np.zeros(nsteps)

#simulate with ODEINT

for i in range(nsteps-1):
    u = step[i]
    # %clip inputs to -50% to 100%
    if u >= 100.0:
        u = 100.0 
    if u <= 50.0:
        u = -50.0
    v = odeint(vehicule, v0, [0,delta_t], args=(u,load))
    v0 = v[-1]  #take the last value


# plot results
plt.figue()
plt.subplot(2,1,1)
plt.plot(ts,vs,'-b',linewidth=3)
plt.plot([0, tf],[25,25],'k--',linewidth=2)
plt.ylabel('Velocity (m/s)')
plt.legend(['Velocity','Set Point'], loc=2)
plt.subplot(2,1,2)
plt.plot(ts,step,'--r', linewidth=3)
plt.ylabel('Gas Pedal')
plt.legend(['GasPedal (%)'])
plt.xlabel('Time (sec)')
plt.show()







    