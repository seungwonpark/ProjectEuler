f = open('p067_triangle.txt','r')
raw = f.read()
raw = raw.replace('\n',' ')
val = raw.split(' ')
arr = [[0 for x in range(0,120)] for y in range(0,120)]
calc = [[0 for x in range(0,120)] for y in range(0,120)]
k = 0
for i in range(1,101):
    for j in range(1,i+1):
        arr[i][j] = int(val[k])
        k += 1;
calc[1][1] = int(val[1])
for i in range(1,101):
    for j in range(1,i+1):
        calc[i][j] = arr[i][j] + max(calc[i-1][j-1],calc[i-1][j])
ans = 0
for i in range(1,101):
    if(calc[100][i] > ans):
        ans = calc[100][i]
print(ans)