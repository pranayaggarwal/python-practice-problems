def check_palindrome(string):
    copy = ''.join(reversed(string))
    if (copy == string):
        print("String {} is a palindrome".format(string))
    else:
        print("String {} is not a palindrome".format(string))


check_palindrome("helleh")


def check_palindrome2(string):
    copy = string[::-1]
    if (copy == string):
        print("String {} is a palindrome".format(string))
    else:
        print("String {} is not a palindrome".format(string))


check_palindrome2("helleh")


