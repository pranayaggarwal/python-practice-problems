# Implement Sieve of Erastothenes

def sqrt(x):
    return x ** 0.5

def chkPrime(x):
    dict = {x: True for x in range(x+1)}

    for num, prime in dict.items():
        if(num > sqrt(x)):
            break

        if (num >=2 and prime):
            # Mark all multiples false
            increment = num
            num+= increment
            while num <= x:
                dict[num] = False
                num+= increment

            if (dict[x] == False):  # optmizations
                return False
    return dict[x]

list = [407, 99, 125, 97]

for item in list:
    print("Prime check for number {} is {}".format(item, chkPrime(item)))