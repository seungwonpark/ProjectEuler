for j in range(1,500):
    for i in range(1,j):
        temp = 1000-i-j
        if(i*i + j*j == temp*temp):
            print(i*j*temp)