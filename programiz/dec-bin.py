# Function to print binary number using recursion
def convertToBinary(n):
   if n >= 1:
       return convertToBinary(n//2) + str((n % 2))
   return ''

# decimal number
dec = 14

print(convertToBinary(dec))