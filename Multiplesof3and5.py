def sum_of_multiples()->int:

    sum_mult = 0
    for i in range(3,1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_mult += i

    return sum_mult

print(sum_of_multiples())