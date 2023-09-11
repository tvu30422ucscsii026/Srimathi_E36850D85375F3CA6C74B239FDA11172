def isLeapyear(year):
   if (year % 4 == 0 and year % 100!= 0) or year % 400 == 0:
      return Truetrue
year=int(input("enter a value"))
if isLeapyear(year):
    print('{} is a Leap year.'.format(year))
else:
    print('{} is not a leapyear.'. format(year))
