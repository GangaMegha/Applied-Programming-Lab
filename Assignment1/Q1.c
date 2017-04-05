#include <stdio.h>

int main()
{
	int first=1;
	int second=1;
	int new,k;

	printf("\n%d",first);

	for(k=3;k<11;k++)
	{	
		printf("\n%d",second);
		
		new=first+second;		//finding next term
		first=second;			
		second=new;
	}
	printf("\n%d",second);
}

	
	
