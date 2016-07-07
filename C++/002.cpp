#include<stdio.h>
#define max 4000000
int fib[100000];
int sum;
int main(){
	fib[1]=1;
	fib[2]=1;
	for(int i=3;;i++){
		fib[i]=fib[i-1]+fib[i-2];
		if(fib[i]>max) break;
		if(fib[i]%2==0) sum+=fib[i];
	}
	printf("%d",sum);
}
