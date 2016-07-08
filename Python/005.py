def gcd(x,y):
	if(x==y):
		return x
	if(x>y):
		return gcd(y,x)
	y-=(int((y-1)/x))*x;
	return gcd(x,y)
def lcm(x,y):
	return int(x*y/gcd(x,y))
ans = 1
for i in range(1,21):
	ans = lcm(ans,i)
print(ans)