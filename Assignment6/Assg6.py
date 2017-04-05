import numpy as np
import scipy as sp
import matplotlib.pylab as mp

#Defining the wire
x1=np.arange(1,0.5,-0.1/(2**0.5))
y1=np.arange(-0.9,-0.4,0.1/(2**0.5))
y2=np.arange(-0.4+0.1,0.5,0.1)
x2=0.5*np.ones(len(y2))
x3=np.arange(0.5,-0.5,-0.1)
y3=0.5*np.ones(len(x3))
y4=np.arange(0.5,-0.5,-0.1)
x4=-0.5*np.ones(len(y4))
x5=np.arange(-0.5,0.4,0.1)
y5=-0.5*np.ones(len(x5))
x6=np.arange(0.4,0.9+0.1/(2**0.5),0.1/(2**0.5))
y6=np.arange(-0.5,-1-0.1/(2**0.5),-0.1/(2**0.5))

x=np.concatenate((x1,x2,x3,x4,x5,x6),axis=0)
y=np.concatenate((y1,y2,y3,y4,y5,y6),axis=0)
conductor=np.vstack((x,y))#(x,y) of end points

mid=(conductor[:,:-1]+conductor[:,1:])/2#midpoints
mid=np.vstack((mid[0,:],mid[1,:],np.zeros(len(mid[0,:]))))

dr_x = np.diff(x)	#dx
dr_y = np.diff(y)	#dy

mp.figure(1)
mp.plot(x,y,'k')
mp.quiver(x,y,dr_x,dr_y,color='b')
mp.scatter(mid[0,:],mid[1,:],c='r')
mp.scatter(conductor[0,:],conductor[1,:],c='k',marker='x')
mp.axis([-1.0,1.0,-1.0,1.0])
mp.savefig('Fig1.png')

dr_x=np.divide(dr_x,(dr_x**2 + dr_y**2)**0.5)
dr_y=np.divide(dr_y,(dr_x**2 + dr_y**2)**0.5)
dl=np.vstack((dr_x,dr_y))	#vector dl

c=np.arange(-1,1.1,0.1)
Y,X,Z=np.meshgrid(c,c,c)
B=np.zeros((21,21,21,3))

for i in range(len(dr_x)) :
	Rx=X-mid[0][i]
	Ry=Y-mid[1][i]
	Rz=Z-mid[2][i]
	R=(Rx**2 + Ry**2 +Rz**2)**1.5
	B[:,:,:,0]+=dr_y[i]*Rz/(R)
	B[:,:,:,1]+=(-dr_x[i]*Rz)/(R)
	B[:,:,:,2]+=(dr_x[i]*Ry - dr_y[i]*Rx)/(R)

mp.figure(2)
mp.quiver(np.arange(-1,1.1,0.1),np.arange(-1,1.1,0.1),B[:,10,:,0].T,B[:,10,:,2].T,scale=2000)
mp.title(r'Arrow plot of $\vec{B}$ along x-z plane')	
mp.xlabel('x')
mp.ylabel('z')
mp.savefig('Fig2.png')

mp.figure(3)
mp.quiver(np.arange(-1,1.1,0.1),np.arange(-1,1.1,0.1),B[:,7,:,0].T,B[:,7,:,2].T,scale=2000)
mp.title(r'Arrow plot of $\vec{B}$ along y=-0.3')	
mp.xlabel('x')
mp.ylabel('z')
mp.savefig('Fig3.png')

mp.figure(4)
mp.quiver(np.arange(-1,1.1,0.1),np.arange(-1,1.1,0.1),B[:,5,:,0].T,B[:,5,:,2].T,scale=1200)
mp.title(r'Arrow plot of $\vec{B}$ along y=-0.5')	
mp.xlabel('x')
mp.ylabel('z')
mp.savefig('Fig4.png')

mp.figure(5)
mp.quiver(np.arange(-1,1.1,0.1),np.arange(-1,1.1,0.1),B[:,3,:,0].T,B[:,3,:,2].T,scale=1000)
mp.title(r'Arrow plot of $\vec{B}$ along y=-0.7')	
mp.xlabel('x')
mp.ylabel('z')
mp.savefig('Fig5.png')

mp.show()
