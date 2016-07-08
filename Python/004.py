def ispalin(x):
	temp = x
	y = 0
	while(int(x)):
		y+=(x%10)
		y*=10
		x/=10
		x = int(x)
	y/=10
	if(temp == y):
		return 1
	else:
		return 0
ans = 0
for i in range(100,1000):
	for j in range(100,1000):
		calc = i*j
		if(ispalin(calc) and calc>ans):
			ans = calc
print(int(ans))