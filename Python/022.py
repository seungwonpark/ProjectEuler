def namevalue(s):
    ans = 0
    for i in range(0,len(s)):
        ans += (ord(s[i])-64)
    return ans
f = open('p022_names.txt','r')
raw = f.read()
names = raw.replace('"','')
list = names.split(',')
list.sort()
ans = 0
for i in range(0,len(list)):
    ans += (i+1)*namevalue(list[i])

print (ans)
    