#include <stdio.h>
#include <math.h>


int main()
{
	double n[1000];
	int k,temp;

	n[0]=0.2;

	double pi=M_PI;			//pi=3.141593	
	
	for(k=1;k<1000;k++)
		n[k] = fmod((n[k-1]+pi)*100.0, 1.0);	//taking the fractional part
	

	for(k=0;k<1000;k++)				//rounding off to 4 decimal places and printing the array
	{
		temp=round(n[k]*10000);
		n[k]=(float)temp/10000;
		//x=float('%.4f%(x));
		printf("%.4f  ", n[k]);		
	}

	return 0;			
}
