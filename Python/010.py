primes = [2]
sum = 2
for i in range(3,2000000):
    isPrime = True
    for j in range(0,len(primes)):
        if(primes[j]*primes[j]>i):
            break
        if(i%primes[j] == 0):
            isPrime = False
            break
    if(isPrime):
        primes.append(i)
        sum += i
print (sum)