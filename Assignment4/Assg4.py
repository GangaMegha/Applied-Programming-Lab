import numpy as np
import math as m
from random import randint
from numpy.random import randn
import matplotlib.pyplot as mp
from scipy.special import jv
from scipy.linalg import lstsq
import scipy as sp

################ Question a #####################

def Jv(x) :	#function computes model (b)
	return(((2/(m.pi*x))**(1/2.0))*sp.cos(x-3*m.pi/4))

x=np.linspace(0,20,num=42)
x=x[1:]
print Jv(x)

################ Question b-f ####################

def fun(x): #function computes matrix [cosx,sinx]		
	Ans=np.zeros((len(x),2))
	Ans[:,0]=sp.cos(x)
	Ans[:,1]=sp.sin(x)
	return Ans

#model a manipulated to get the further models
def calcnu(x,x0,color,eps,model):
	A=np.zeros((41,2))
	v=[]
	for i in x0 :
		y=x[np.where(x>=i)]	#only required x
		A=fun(y)

		if model=='b' :
			A[:,0]=A[:,0]/((y)**(1/2.0))
			A[:,1]=A[:,1]/((y)**(1/2.0))

		J=jv(1.0,y)	#in-build bessel function 

		if model=='b' :
			noise=eps*randn(len(J))
			J+=noise	#adding noise to J
		
		B=lstsq(A,J)[0]	#computes coefficients

		C=B[0]/((B[0]*B[0] + B[1]*B[1])**(1/2.0))
		C=sp.arccos(C)
		v.append((C-m.pi/4)*2/m.pi)	#computes v

	l, =mp.plot(x0,v,color)	
	line.append(l)	#for displaying all plots

for i in range(8): #for varying the measurements
	number=randint(10,60)
	x0=np.linspace(0.1,18,num=number)
	line=[]
	calcnu(x,x0,'go',0,'a')
	calcnu(x,x0,'bo',0,'b')
	calcnu(x,x0,'ro',0.01,'b')

	mp.legend([line[0],line[1],line[2]],\
		[r'$\epsilon =0$,model (b)',r'$\epsilon =0$,model (c)',\
		r'$\epsilon=10^{-2}$,model (c)'], loc='lower right')
	mp.xlabel('x0')
	mp.ylabel('Predicted v')
	mp.title('Plot of v')
	mp.savefig('Fig{}.png'.format(i+1))
	mp.show()