#python program to check leap year
Year =int(input("2012"))
if(year%4==0 and year%100==0 or year%400==0):
  Print("the year is a leap year!")
else:
  Print("the year is not leap year !")