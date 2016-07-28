#include<stdio.h>
int primes[10000]; // primes under 10000
int primecount;
int geometric(int prime, int exponent){
    int i;
    int sum = 0;
    sum++;
    for(i=1;i<=exponent;i++){
        sum*=prime;
        sum++;
    }
    return sum;
}
int factorproduct(int num){
    int i;
    int product = 1;
    for(i=1;;i++){
        if(num==1) break;
        if(primes[i]*primes[i]>num){
            product *= (1+num); // num is prime
            break;
        }
        int exponent = 0;
        while(num%primes[i]==0){
            exponent++;
            num /= primes[i];
        }
        product *= geometric(primes[i],exponent);
    }
    return product;
}
int realfactorproduct(int num){
    return factorproduct(num)-num;
}
int main(){
    int n,i,j;
    n = 10000;
    primes[1]=2;
    primecount=1;
    int ans = 0;
    for(i=3;i<=10000;i+=2){
        bool isPrime = true;
        for(j=1;j<=primecount;j++){
            if(primes[j]*primes[j]>i){
                break;
            }
            if(i%primes[j]==0){
                isPrime = false;
                break;
            }
        }
        if(isPrime == true){
            primes[++primecount]=i;
        }
    }
    for(i=2;i<=n;i++){ // to prevent showing (1,0)
        if(realfactorproduct(realfactorproduct(i)) == i){
            if(realfactorproduct(i) != i){
                ans += i;
            }
        }
    }
    printf("%d",ans);
}