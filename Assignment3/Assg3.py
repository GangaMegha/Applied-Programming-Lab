from pylab import *
import re
import numpy as np
from scipy.integrate import quad

def f1(x):
	return exp(x)

def f2(x):
	return cos(cos(x))

def f1_sin(n):
	ans= lambda x,a : exp(x)*sin(n*x)
	return ans

def f1_cos(n):
	ans= lambda x,a : exp(x)*cos(n*x)
	return ans

def f2_sin(n):
	ans= lambda x,a : cos(cos(x))*sin(n*x)
	return ans

def f2_cos(n):
	ans= lambda x,a : cos(cos(x))*cos(n*x)
	return ans

################################################# Question 1 ##########################################################

x = raw_input("Enter the vector x for Q1 : ")	#accept a vector x from the user in any form
x=re.sub('[^0-9 ]+', ' ',x)						#remove all characters except for digits and spaces from the string
x=x.split()										#split the string 
x=[float(a) for a in x]							#convert each element of list to float
x=np.array(x)									#making it an array

y1=f1(x)			#finding exp(x)
y2=f2(x)			#finding cos(cosx)

#printing out exp(x) and cos(cosx)
print("\nexp(x) given as : {} \n\ncos(cos(x)) is given as : {}\n\nwhere x is taken in radians\n\n".format(y1,y2))

################################################# Question 2 ###########################################################

expx=[]	#coefficient vector for exp(x)
coscosx=[]#coefficient vector for cos(cosx)

temp=quad(f1_cos(0),0,2*pi,args=(0))
expx.append(temp[0]/(2*pi)) #compute a0
temp=quad(f2_cos(0),0,2*pi,args=(0))
coscosx.append(temp[0]/(2*pi)) #compute a0

for i in range(1,26):	#loop for computing values of the coefficients
	temp=quad(f1_cos(i),0,2*pi,args=(i)) #computes a0 for exp(x)
	expx.append(temp[0]/pi)
	temp=quad(f2_cos(i),0,2*pi,args=(i)) #computes a0 for cos(cosx)
	coscosx.append(temp[0]/pi)

	temp=quad(f1_sin(i),0,2*pi,args=(i)) #computes b0 for exp(X)
	expx.append(temp[0]/pi)
	temp=quad(f2_sin(i),0,2*pi,args=(i))#computes b0 for cos(cosx)
	coscosx.append(temp[0]/pi)
	
with open('Output.txt','a') as file_obj:
	file_obj.write("\nThe 51 coefficients for exp(x): {}".format(expx))	
	file_obj.write("\n\nThe 51 coefficients for cos(cos(x)): {}".format(coscosx))

################################################ Question 3 ##########################################################
expx=np.array(expx)
coscosx=np.array(coscosx)

temp=linspace(1,25,num=25,endpoint=True)#defining a list ranging from 1 o 25

n=np.zeros(51)	#n denotes x axis ->different frequencies

n[1::2]=temp #n will have one 0 and then doublets of the 
n[2::2]=temp #rest of the numbers till 25

line1, = semilogy(n,abs(expx),'ro',linewidth=10)
xlabel('n')
ylabel('Coefficients')
title("3a) semilog for exp(x)")
savefig("3a.png")
show()

line2, = loglog(n,abs(expx),'ro',linewidth=10)
xlabel('n')
ylabel('Coefficients')
title("3b) loglog for exp(x)")
savefig("3b.png")
show()

line3, = semilogy(n,abs(coscosx),'ro',linewidth=10)
xlabel('n')
ylabel('Coefficients')
title("3c) semilog for cos(cos(x))")
savefig("3c.png")
show()

line4, = loglog(n,abs(coscosx),'ro',linewidth=10)
xlabel('n')
ylabel('Coefficients')
title("3d) loglog for cos(cos(x))")
savefig("3d.png")
show()

############################################### Question 3 ###############################################

x = linspace(0,2*pi,num=401)	#creating x for least square approximation
x=x[:-1]		 # drop last term to have a proper periodic integral
b1=f1(x)		 # f1->exp() has been written to take a vector
b2=f2(x)		 # f2->cos(cosx) has been written to take a vector

with open('Output.txt','a') as file_obj:
	file_obj.write(("\nexp(x) given as : {} \n\ncos(cos(x)) is given as : {}\n\nwhere x is taken in radians\n\n".format(b1,b2)))

A1=np.zeros((400,51))	 # allocate space for A1->exp(x)
A2=np.zeros((400,51))	 # allocate space for A2->cos(cosx)

A1[:,0]=1 	 # col 1 is all one
A2[:,0]=1 	 # col 1 is all one

for k in range(1,26):
	A1[:,2*k-1]=cos(k*x)	# cos(kx) column
	A2[:,2*k-1]=cos(k*x)	# sin(kx) column

	A1[:,2*k]=sin(k*x)		# cos(kx) column
	A2[:,2*k]=sin(k*x)		# sin(kx) column

c11=lstsq(A1,b1)[0]
c12=lstsq(A2,b2)[0]

line5, = semilogy(list(range(0,51)),abs(c11),'go',linewidth=10)
xlabel('n')
ylabel('Coefficients')
title("8a) semilogy for exp(x)")
savefig("8a.png")
show()

line6, = semilogy(list(range(0,51)),abs(c12),'go',linewidth=10)
xlabel('n')
ylabel('Coefficients')
title("8b) semilogy for cos(cos(x))")
savefig("8b.png")
show()

line7, = loglog(list(range(0,51)),abs(c11),'go',linewidth=10)
xlabel('n')
ylabel('Coefficients')
title("8c) loglog for exp(x)")
savefig("8c.png")
show()

line8, = loglog(list(range(0,51)),abs(c12),'go',linewidth=10)
xlabel('n')
ylabel('Coefficients')
title("8d) loglog for cos(cos(x))")
savefig("8d.png")
show()

################################### Question 6 #######################################

error_exp=abs(c11-expx)		#deviation for exp(x)
error_cos=abs(c12-coscosx)	#deviation for cos(cosx)

line9, = semilogy(n,error_exp,'ro',linewidth=10)
xlabel('n')
ylabel('Error')
title("9a) Error for exp(x) - Semilogy")
savefig("9a.png")
show()

line10, = semilogy(n,error_cos,'ro',linewidth=10)
xlabel('n')
ylabel('Error')
title("9b) Error for cos(cosx)- Semilogy")
savefig("9b.png")
show()

with open('Output.txt','a') as file_obj:
	file_obj.write("\n\nMaximum deviation for exp(x) is {} and cos(cosx) is {}".format(max(error_exp),max(error_cos)))