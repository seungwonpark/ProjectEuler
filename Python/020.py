product = 1
for i in range(1,101):
    product *= i
string = str(product)
ans = 0
for j in range(0,len(string)):
    ans += int(string[j])
print (ans)