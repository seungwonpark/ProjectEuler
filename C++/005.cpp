#include<stdio.h>
#define lli long long int
lli gcd(lli a, lli b){
	if(a==b) return a;
	if(a>b) return gcd(b,a);
	b-=((lli)((b-1)/a))*a;
	return gcd(a,b);
}
lli lcm(lli a, lli b){
	return (lli)(a*b/gcd(a,b));
}
int main(){
	lli ans = 1;
	for(int i=1;i<21;i++){
		ans = lcm(ans,i);
	}
	printf("%lld",ans);
}