a=1
b=1
i=2
sum=0
while(1):
	i+=1
	c=a+b
	a=b
	b=c
	if(c>4000000):
		break
	if(c%2==0):
		sum+=c
print (sum)