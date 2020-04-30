def fib_even():
    i = 0
    j = 1
    k = i + j
    sum_even = 0
    while k <= 4000000:
        i = j
        j = k
        k = i + j
        if k % 2 == 0:
            sum_even += k
    print(sum_even)