import numpy as np
import matplotlib.pyplot as plt

#Physical constants
h = 6.626e-34
c = 2.99e+8
k = 1.38e-23

#Planck function in terms of frequency (nu)
def Bnu(nu,t0):
    a0 = 2.0*h/(c**2)
    b0 = h*nu/(k*t0)
    return (a0*nu**3)*(np.exp(b0)-1)**-1
nu = np.arange(1e13,3e16,1e12)

#FIGURE1
fig1 = plt.figure(figsize=(10,10))
#fmt = FormatStrFormatter('%.3f')
major_ticks = np.arange(0,3000,400)
minor_ticks = np.arange(0,3000,100)
major_ticks2 = np.arange(0,20,2)
minor_ticks2 = np.arange(0,20,1)

#Temperatures of Blackbodies
t1 = 4000
t2 = 5800 #Temperature of the Sun
t3 = 7000
t4 = 7500

ax = fig1.add_subplot(1,1,1)
ax.plot(1e-12*nu,1e12*1e-4*Bnu(nu,t1),c='r',alpha=0.8,label='T$_{1}$ = %.1f K' %(t1))
ax.plot(1e-12*nu,1e12*1e-4*Bnu(nu,t2),c='gold',alpha=0.8,label='T$_{2}$ = %.1f K' %(t2))
ax.plot(1e-12*nu,1e12*1e-4*Bnu(nu,t3),c='b',alpha=0.8,label='T$_{3}$ = %.1f K' %(t3))
ax.plot(1e-12*nu,1e12*1e-4*Bnu(nu,t4),c='m',alpha=0.8,label='T$_{4}$ = %.1f K' %(t4))
ax.tick_params(which='major',direction='in',top=True,right=True,width=2,length=10,labelsize=18)
ax.tick_params(which='minor',direction='in',top=True,right=True,width=1,length=5,labelsize=18)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks2)
ax.set_yticks(minor_ticks2, minor=True)
plt.xlabel('$\\nu$ [THz]',fontsize=25)
plt.ylabel('B$_{\\nu}$ [10$^{4}$ W m$^{-2}$ sr$^{-1}$ THz$^{-1}$]',fontsize=25)
plt.xlim(0,3000)
plt.ylim(0,11)
ax.legend(scatterpoints=1,loc='upper right',fontsize=18,columnspacing=1.0)

plt.show()
