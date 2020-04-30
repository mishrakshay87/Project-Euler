def prime_product():
    l = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if ispalindrome(i*j):
                l.append(i*j)
    return max(l)

def ispalindrome(n)->bool:

        str_n = str(n)
        l = 0
        r = len(str_n)-1

        while l < r:
            if str_n[l] == str_n[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

print(prime_product())
