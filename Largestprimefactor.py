def largest_prime(n):

    l1 = []

    max_factor = 0
    i = 2
    even_flag = 0
    while n % i == 0:
        even_flag = 1
        n = int(n / i)
    if even_flag == 1:
        l1.append(2)

    for j in range(3,int(pow(n,0.5))+1,2):
        while n % j == 0:

            l1.append(j)d
            n = int(n / j)

    if n > 2:
        l1.append(n)
    print(max(set(l1)))