# Program to add two matrices using nested loop
def mulMatrix(x, y):

    result = [[0 for j in range(len(Y[0])) ] for i in range(len(X))]

    for row in range(len(X)):
        for col in range(len(Y[0])):
            for k in range(len(Y)):
                result[row][col] += X [row][k] * Y[k][col]

    return result

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

for row in mulMatrix(X, Y):
    print(row)
