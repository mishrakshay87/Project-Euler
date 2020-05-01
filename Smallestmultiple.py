def find_gcd(a,b):

    if b == 0:
        return a

    if a < b:
        a,b = b,a
    r = a % b
    return find_gcd(b,r)



def smallest_product(n):

    prod = n
    gcd = 0
    lcm = 0
    lcm = 1
    for i in range(1,n):
        gcd = find_gcd(lcm,i+1)
        lcm = int(lcm*(i+1)/gcd)
    print(lcm)