val = 1 # Monday at 1900.01.01
monthnorm = [0, 31,28,31, 30,31,30, 31,31,30, 31,30,31]
monthleap = monthnorm
monthleap[2] = 29

val += 365 # 1900 is not leap year
ans = 0

for i in range(1,101):
    if(i%4 != 0):
        arr = monthnorm
    else:
        arr = monthleap
    for j in range(1,13):
        if(val%7 == 0):
            ans += 1
        val += arr[j]
print (ans)