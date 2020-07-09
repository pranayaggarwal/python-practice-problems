

def printArmstrongInRange(start, end):

    list = []
    for i in range(start, end + 1):
        num = i;

        order = len(str(num))

        sum = 0
        while num > 0:
            digit = num % 10
            num //= 10
            sum = sum + digit ** order
        
        if (sum == i):
            list.append(i)
    
    return list


print("Armstrong number is between this range ({}-{}) is {}".format(100, 2000, printArmstrongInRange(100, 2000)))