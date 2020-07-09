from decimal import Decimal

def sqrt(x):
    return x ** 0.5

def area(lis):
    s = sum(lis)/2
    product = s;
    for item in lis:
        product = product * (s-item)
    # ans = round(sqrt(product), 2)  # plain round can be misleading
    ans = round(Decimal(sqrt(product)), 2)
    return ans

list = []
sides = 3
for i in range(sides):
    list.append(int(input("Enter side no# {} = ".format(i+1))))

print("Area of triangle is ", area(list))