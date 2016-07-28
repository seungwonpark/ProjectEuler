# 40C20
ans = 1
for i in range(1,21):
    ans *= (41-i);
    ans /= i;
print (int(ans))