# Leap year is divisble by 4
# Not a leap year if divisble by 100
#    - Except the ones that are divisible by 400


def checkLeapYear(year):
    if ((year % 400 == 0) or (year % 4 == 0 and year % 100 is not 0)):
        return True
    return False


list = [1900, 2017, 2012, 2000]
for year in list:
    print("Leap year check for", year, "is", checkLeapYear(year))



