def generate_primes(n):

    i = 2
    count = 0
    flag = 1
    while count < n:

        for j in range(2,int(pow(i,0.5))+1):

            if i % j == 0:
                flag = -1
                break
        if flag == 1:
            count += 1
        flag = 1
        i += 1

    print(i-1)