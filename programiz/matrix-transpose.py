# Program to add two matrices using nested loop
def transposeMatrix(X):

    result = [[0 for j in range(len(X)) ] for i in range(len(X[0]))]

    for row in range(len(X)):
        for col in range(len(X[row])):
            result[col][row] = X[row][col]

    return result

X = [[12,7],
    [4 ,5],
    [7 ,8]]

for row in transposeMatrix(X):
    print(row)



print('\n\n')
# Using advance list comprehension

def transposeMatrixAdvanced(X):

    result = [[ X[j][i] for j in range(len(X)) ] for i in range(len(X[0]))]
    return result


for row in transposeMatrixAdvanced(X):
    print(row)