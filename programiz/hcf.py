def gcd(a,b):
    if (a > b):
        return gcd(b, a)
    while (b):
        a,b = b, a % b
    return a


print("GCD of 300, 375 is", gcd(375, 350))