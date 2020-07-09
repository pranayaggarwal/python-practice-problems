# to swap values

x = 5
y = 10

print("Before swapping values are {} and {}".format(x, y))
x, y = y, x


print("After swapping values are {} and {}".format(x, y))


# Let's try with a function now
# whatevr we swap will be within the scope of function


x = 5
y = 10

def swap(x, y):
    return y, x


print("Before swapping values are {} and {}".format(x, y))

x, y = swap(x, y)

print("After swapping values are {} and {}".format(x, y))
