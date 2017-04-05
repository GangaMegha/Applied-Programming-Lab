import re
import numpy as np
import scipy as sp
from scipy.integrate import quad
import matplotlib.pyplot as mp

def integrand(t) :							#function to carry out integration
	ans= 1.0/(1+t*t)
	return ans

def format(list):
	return "["+", ".join(["%.5f" % x for x in list])+"]"

def integ_fun() :							#function describing the integration function
	ans= lambda t : 1.0/(1+t*t)
	return ans

def taninv(x) :								#function for Q4
	result=quad(integ_fun(),0,x)
	return result

############################# Question 1 ##################################

t=raw_input("Enter vector x for Qn.1 : ")
											# process string elements in the list and make them integers
t=re.sub('[^0-9 ]+', ' ', t)				#remove unwanted characters
t = t.split() 								#splits the input string on spaces
t = [float(a) for a in t] 					#convert to floating point list
ans=integrand(np.array(t))					#calling the function
print "\n1.)Answer : " 
ans=format(ans)
print ans

############################# Question 2 ####################################

x,h=np.linspace(0,5,num=51,endpoint=True,retstep=True) 
print "2.)Array Created X: " 
print x
print "\n Steps :%f" % h

############################# Question 3 ####################################

mp.plot(x,integrand(x),'r--')
mp.xlabel('Vector x')
mp.ylabel('f(x)')
mp.title(r"3.)Plot of $1/(1+x^{2})$")
mp.savefig("Q3.png")
mp.show()

############################# Question 4 #####################################

tan_inv1=[]
error=[]

for i in x :																			#Question 4a
	k=taninv(i)
	tan_inv1.append(k[0])
	error.append(k[1])

print "\nQ 4a.)The vector of integrals : ",tan_inv1

x=np.array(x)																			#Question 4b
tan_inv2=(np.arctan(x))

print "\nQ 4b.)Calculated\tTheoretical\n     -------------------------------"
print "\n".join("     {0}\t{1}".format(a, b) for a, b in zip(tan_inv1, tan_inv2))

line1, =mp.plot(x,tan_inv1,'ro',linewidth=10)											#Question 4c
line2, =mp.plot(x,tan_inv2,'k')
mp.legend([line1,line2],['Quad fn',r'$tan{^{-1}}x$'],loc='center right')
mp.xlabel('Vector x')
mp.ylabel(r'$\int_{0}^{x} 1/(1+u^{2}) du$')
mp.title("Figure 1")
mp.savefig("4c.png")
mp.show()

mp.semilogy(x, error,'ro', lw=2)														#Question 4d
mp.xlabel('Vector x')
mp.ylabel("Error")
mp.title(r'Error in $\int_{0}^{x} 1/(1+u^{2}) du$')
# mp.savefig("4d.png")
mp.show()

############################## Question 5 #####################################

I=[]
s=0.0
n=len(x)

for i in range(0,n) :																		#Question 5a
	s+=integrand(x[i])
	I.append((s-0.5*(integrand(x[0])+integrand(x[i])))*h)

print "\n\na.)The integral value using for loop : \n" ,I

I=np.zeros(len(x))																			#Question 5b
y=sp.cumsum(integrand(x))
I=(y-(0.5)*(integrand(x)+integrand(0)))*h

print "\n\nb.)The integral value using cumsum : \n",I

line3, =mp.plot(x,tan_inv1,'ro',linewidth=10)
line4, =mp.plot(x,tan_inv2,'k')
line5, =mp.plot(x,I,'b+',linewidth=40)
mp.legend([line3,line4,line5],['Quad fn',r'$tan{^{-1}}x$','Trapezoidal'],loc='center right')
mp.xlabel('Vector x')
mp.ylabel(r'$\int_{0}^{x} 1/(1+u^{2}) du$')
mp.title("5b.) Figure 1")
mp.savefig("5b.png")
mp.show()

h_array=[]																					#Question 5c
apprx_error=[]
exact_error=[]
temp=10			#temp stores the last value in exact_error
I1=I 			#holds previous integration
I2=I 			#holds current integration

while temp>pow(10,-8) :				#tolerance taken as 10^(-8)

	h_array.append(h)
	temp=max(abs(np.arctan(x)-np.array(I2)))	#calculating the exact error
	exact_error.append(temp)
	
	h=h/2		#Changing h value

	x,h=np.linspace(0,5,num=5/h+1,endpoint=True,retstep=True)		#forming the new x 
	
	y=sp.cumsum(integrand(x))
	I2=(y-(0.5)*(integrand(x)+integrand(x[0])*np.ones(len(x))))*h 	#computing the new integration 

	I3=I2[::2]-I1 	#difference between the current and previous integration vector

	I1=I2 			#re-initialising I1 to the current integration vector

	apprx_error.append(max(I3))		#calculating the approximate error
	

print "\n\n\nApproximate error :\n",apprx_error
print"\n\n\nExact error :\n",exact_error


mp.yscale('log')
mp.xscale('log')
mp.xlabel('h')
mp.ylabel('Error')
line6, =mp.plot(h_array,exact_error,'ro',linewidth=10)
line7, =mp.plot(h_array,apprx_error,'g+',linewidth=10)
mp.legend([line6,line7],['Exact error','Estimated error'],loc='upper left')
mp.title("5c.) Figure 2")
mp.savefig("5c.png")
mp.show()