import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def fun(x,y):
    return 1-x-y
fig1=plt.figure()
ax=Axes3D(fig1)
X,Y=np.mgrid[-5:5:40j,-5:5:40j]
# X=np.arange(-5,5,0.01)
# Y=np.arange(-5,5,0.01)
#Z=np.arange(-5,5,0.01)
Z=fun(X,Y)
plt.title('function z=1-x-y')
ax.plot_surface(X,Y,Z,rstride=1,cstride=1)
ax.set_xlabel('X',color='r')
ax.set_ylabel('Y',color='g')
ax.set_zlabel('Z',color='b')
#plt.slabel('S',fontdict=14)
#plt.tick_params(axis='both',labelsize=14)
plt.show()
