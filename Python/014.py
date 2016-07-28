data = {0:0, 1:1}
#print (data[0])
max = 0
def collatz(n):
    if n in data:
        x = 1
    else:
        if(n%2 == 0):
            data[n] = 1 + collatz(int(n/2))
        else:
            data[n] = 1 + collatz(3*n+1)
    return data[n]
for i in range(1,1000000):
    temp = collatz(i)
    if(temp>max):
        max = temp
        ans = i
print (ans)