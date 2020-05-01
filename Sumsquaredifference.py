def square_diff(n):

    sq_sum = 0
    sum_n = 0

    sq_sum = n * (n+1)*(2*n+1)/6
    sum_n = n*(n+1)/2

    print(int(pow(sum_n,2)-sq_sum))


square_diff(100)