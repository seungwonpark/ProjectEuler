n = 600851475143
i=3;
# better to use while loop than for loop
# it seems to be that python has no thing like : for(i=1;;i++)
while(i*i < n):
	while(n%i==0):
		n/=i
	i+=2
print(int(n))