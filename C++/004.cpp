#include<stdio.h>
int ispalin(int x){
	int temp;
	temp = x;
	int y=0;
	while(x){
		y+=(x%10);
		y*=10;
		x/=10;
	}
	y/=10;
	if(temp == y) return 1;
	else return 0;
}
int ans;
int main(){
	for(int i=100;i<1000;i++){
		for(int j=100;j<1000;j++){
			if(ispalin(i*j) && i*j>ans) ans=i*j;
		}
	}
	printf("%d",ans);
}