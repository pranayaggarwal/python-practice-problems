# Program to add two matrices using nested loop
def addMatrix(x, y):

    result = [[0 for j in range(len(X[0])) ] for i in range(len(X))]
    for row in range(len(X)):
        for col in range(len(X[row])):
            result[row][col] = X [row][col] + Y[row][col]

    return result

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

for row in addMatrix(X, Y):
    print(row)



print('\n\n')
# Using advance list comprehension

def addMatrixAdvanced(X, Y):

    result = [[  X [i][j] + Y[i][j] for j in range(len(X[0])) ] for i in range(len(X))]
    return result

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

for row in addMatrixAdvanced(X, Y):
    print(row)
