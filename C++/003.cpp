#include<stdio.h>
#define val 600851475143
int main()
{
	long long int n = val;
	// trivially, not divided by 2
	for(int i=3;;i+=2){
		if(i*i>n) break;
		while(n%i==0) n/=i;
	}
	printf("%lld",n);
}