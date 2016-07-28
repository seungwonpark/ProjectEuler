product = 2**1000
digits = str(product)
ans = 0
for i in range (0,len(digits)):
    ans += int(digits[i])
print (ans)