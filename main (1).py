year = 2019

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a Leap year")
else:
    print("The year is not a Leap year")