primes = [2]
for i in range(3,10000000000000):
    if(i%2 == 0):
        continue
    for j in range(0,len(primes)):
        isPrime = True
        if(primes[j]*primes[j] > i):
            break
        if(i%primes[j] == 0):
            isPrime = False
            break
    if(isPrime):
        primes.append(i)
    if(len(primes) == 10001):
        print(primes[len(primes)-1])
        break