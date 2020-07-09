def printTable(x):
    for i in range(1,11):
        print("{} x {} = {}".format(x, i , x*i))


printTable(12)


# ================================================ fac ================================================ #


def getFactorial(x):
    fac = 1
    for i in range(1, x+1):
        fac = fac * i;
    return fac




list = [10, 7]
for num in list:
    print("Factorial for number = ", num, "is", getFactorial(num))

