import numpy as np 
import scipy.signal as sp
import matplotlib.pyplot as mp

def fun(a,b) : 
	X=sp.lti(np.polymul([1,a],[1]),np.polymul([1,2*a, (b**2) + (a**2)],[1,0,2.25]))
	t,x=sp.impulse(X,0,np.linspace(0,50,101))
	t2,x2=sp.impulse(X,0,np.linspace(0,500,1001))

	fig0,ax0=mp.subplots(2)
	fig0.suptitle("Frequency of cosine={} and decay={}".format(b,a))
	ax0[0].plot(t,x)
	ax0[0].set_title("Time till 50s")
	ax0[1].plot(t2,x2)
	ax0[1].set_title("Time till 500s")
	mp.show()

fun(0.5,1.5)	#Question 1
fun(0.05,1.5)	#Question 2

#Question 3
b=1.4
for i in range(5) :
	fun(0.05,b)
	b+=0.05

#Question 4
Y=sp.lti([2],[1,0,3,0,0])
X=sp.lti([1,0,2,0],[1,0,3,0,0])

t,y=sp.impulse(Y,np.array([[0],[0],[0],[0]]),np.linspace(0,20,1001))
t,x=sp.impulse(X,np.array([[0],[0],[0],[1]]),np.linspace(0,20,1001))

fig1,ax1=mp.subplots(2)
fig1.suptitle("Coupled spring")
ax1[0].plot(t,x)
ax1[0].set_title('For x(t)')
ax1[1].plot(t,y)
ax1[1].set_title("For y(t)")

#Question 5
L=1/1000000.0
C=1/1000000.0
R=100.0
H=sp.lti([1],[L*C,R*C,1])
w,S,phi=H.bode()
fig2,ax2=mp.subplots(2)
fig2.suptitle("Steady state Transfer FUnction of two-port network")
ax2[0].semilogx(w,S)
ax2[0].set_title('Bode Magnitude Plot')
ax2[1].semilogx(w,phi)
ax2[1].set_title("Bode Phase Plot")

#Question 6
t=np.linspace(0,0.000035,num=1000)
vi=np.cos(1000*t)-np.cos(1000000*t)
t,y,svec=sp.lsim(H,vi,t)
mp.figure(3)
mp.plot(t,y)
mp.title(r'Plot of $v_{0}$(t)=$v_{i}$(t) * h(t)')
mp.xlabel("t")
mp.ylabel(r'$v_{0}$(t)')
mp.show()
