sumsq = 0
sum = 0
for i in range(1,101):
	sumsq += i*i
	sum += i
print (sum*sum-sumsq)