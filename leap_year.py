#verific if is leap year
#Enter, only, with year
#

def is_leap(year):
    leap = False
    if ((year%400 == 0) & (year%4 == 0)):
        return not leap
    elif ((year%100 != 0) & (year%4 == 0)):
        return not leap
    elif year%100 == 0:
        return leap
    elif (year%400 != 0) | (year%4 != 0):
        return leap
year = int(input())
print(is_leap(year))