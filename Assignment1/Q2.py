import math

def format(list):
	return "["+", ".join(["%.4f" % x for x in list])+"]"

n=[]
n.append(0.2)
pi=math.pi 			# pi=3.14159265359

for k in range(1,1000) :
	frac, whole = math.modf((n[k-1]+pi)*100)	#taking the fractional part
	n.append(frac)
	
n=format(n)		#setting  the precision
print n