import numpy as np
import matplotlib.pyplot as plt

#Physical constants
h = 6.626e-34
c = 2.99e+8
k = 1.38e-23

#Planck function
def Blam(lam,t0):
    a0 = 2.0*h*c**2
    b0 = h*c/(lam*k*t0)
    return (a0/(lam)**5)*(np.exp(b0)-1)**-1
lam = np.arange(1e-9,3e-6,1e-9)

#FIGURE1
fig1 = plt.figure(figsize=(10,10))
#fmt = FormatStrFormatter('%.3f')
major_ticks = np.arange(0,3000,200)
minor_ticks = np.arange(0,3000,100)
major_ticks2 = np.arange(0,20,2)
minor_ticks2 = np.arange(0,20,1)

#Temperatures of Blackbodies
t1 = 4000
t2 = 5800 #Temperature of the Sun
t3 = 7000
t4 = 7500

ax = fig1.add_subplot(1,1,1)
ax.plot(1e9*lam,1e-9*1e-4*Blam(lam,t1),c='r',alpha=0.8,label='T$_{1}$ = %.1f K' %(t1))
ax.plot(1e9*lam,1e-9*1e-4*Blam(lam,t2),c='gold',alpha=0.8,label='T$_{2}$ = %.1f K' %(t2))
ax.plot(1e9*lam,1e-9*1e-4*Blam(lam,t3),c='b',alpha=0.8,label='T$_{3}$ = %.1f K' %(t3))
ax.plot(1e9*lam,1e-9*1e-4*Blam(lam,t4),c='m',alpha=0.8,label='T$_{4}$ = %.1f K' %(t4))
ax.tick_params(which='major',direction='in',top=True,right=True,width=2,length=10,labelsize=18)
ax.tick_params(which='minor',direction='in',top=True,right=True,width=1,length=5,labelsize=18)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks2)
ax.set_yticks(minor_ticks2, minor=True)
plt.xlabel('$\lambda$ [nm]',fontsize=25)
plt.ylabel('B$_{\lambda}$ [10$^{4}$ W m$^{-2}$ nm$^{-1}$ sr$^{-1}$]',fontsize=25)
plt.xlim(0,1600)
plt.ylim(0,11)
ax.legend(scatterpoints=1,loc='upper right',fontsize=18,columnspacing=1.0)

plt.show()
