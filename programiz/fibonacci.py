def listFib(term):
    list = [0, 1]
    x = 0
    y = 1

    for term in range(3, term+1):
        x, y = y, x + y
        list.append(y)
    
    return list


print(listFib(10))