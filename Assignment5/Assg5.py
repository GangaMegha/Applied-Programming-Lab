from pylab import *
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import sys

def update(phi):	#Updating the potential
	phi[1:-1,1:-1]=0.25*(phi[:-2,1:-1]+\
		phi[1:-1,0:-2]+phi[2:,1:-1]+phi[1:-1,2:])
	return phi

def assert_boundaries(phi,Nbegin,Nend):	#boundary conditions
	phi[1:-1,0]=phi[1:-1,1]
	phi[1:-1,-1]=phi[1:-1,-2]
	phi[0,1:Nbegin],phi[0,Nend+1:-1]=phi[1,1:Nbegin],phi[1,Nend+1:-1]
	phi[-1,1:Nbegin],phi[-1,Nend+1:-1]=phi[-2,1:Nbegin],phi[-2,Nend+1:-1]
	return phi


def fun(Nx=25,Ny=25,Nbegin=8,Nend=17,Niter=1500) :
	error=zeros(Niter)

	phi=zeros((Nx,Ny))		#create phi matrix
	phi[0,Nbegin:Nend+1]=1 	#top potential 1
	phi[-1,Nbegin:Nend+1]=0	#lower potential 0

	for k in range(Niter):
		oldphi=phi.copy()
		phi=update(phi)
		phi=assert_boundaries(phi,Nbegin,Nend)
		error[k]=(abs(phi-oldphi)).max()

	logy=log(error)	
	x=np.ones((len(error),2))
	x[:,1]=range(Niter)
	
	ans1=lstsq(x,logy)[0] #from index 0
	ans2=lstsq(x[500:,:],logy[500:])[0] #from index 500
	
	A1,B1=exp(ans1[0]),ans1[1]
	A2,B2=exp(ans2[0]),ans2[1]
	
	q1 = B1*np.arange(Niter)
	q2=B2*np.arange(Niter)

	print "A and B values for error : "
	print "Case 1 : {} and {}".format(A1,B1)
	print "Case 2 : {} and {}".format(A2,B2)
	
	title('Evaluation of Error with iteration')
	xlabel('Iteration')
	ylabel('log(Error)')
	semilogy(range(Niter)[::50],error[::50],'ro',label='error')
	semilogy(range(Niter)[::50],A1*np.exp(q1)[::50],'r',label='fit1')
	semilogy(range(Niter)[500::50],A2*np.exp(q2)[500::50],'g',label='fit2')
	legend()
	show()

	fig1=figure(4) 
	ax=p3.Axes3D(fig1)
	x=arange(1,Nx+1)
	y=arange(1,Ny+1)
	X,Y=meshgrid(x,y)
	title('The 3D Surface plot of the potential')
	surf=ax.plot_surface(Y,X,phi,rstride=1,cstride=1,cmap=cm.jet,linewidth=0)
	show()

	title('Contour plot of potential')
	contour(Y,X,phi)
	show()

	Jx=np.zeros(phi.shape) 	#current densities
	Jy=Jx.copy()

	Jx[1:-1,1:-1]=(phi[1:-1,:-2]-phi[1:-1,2:])/2
	Jy[1:-1,1:-1]=(phi[:-2,1:-1]-phi[2:,1:-1])/2

	title('Vector plot of the current flow')
	quiver(y,x,Jy.transpose(),Jx.transpose())
	show()
	print "Electrode between indices : {} and {}".format(Nbegin,Nend)
	print "The Iavg value : {}".format((sum(Jy[:,1]) + sum(Jy[:,-2]))/2)  #Iavg
	print "The Idiff value : {}".format(abs(sum(Jy[:,1]) - sum(Jy[:,-2])))	#Idiff
	print "Resistance : {}".format(1/((sum(Jy[:,1]) + sum(Jy[:,-2]))/2)) #V/Iavg
	return phi,Nx,Ny

#Order : Nx,Ny,Nbegin,Nend,Niter
fun()
fun(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),\
	int(sys.argv[4]),int(sys.argv[5]))	#for fist case with small electrode
phi,Nx,Ny=fun(int(sys.argv[1]),int(sys.argv[2]),0,\
	int(sys.argv[2])-1,int(sys.argv[5]))	#long electrode

array=np.zeros(phi.shape)	#Computing error
arr=np.linspace(Ny,Ny,Ny)-np.arange(0,Ny)
array=arr
epsilon2=sum((phi-array/Ny)**2)/(Nx*Ny)
print 'epsilon2 = {}'.format(epsilon2)