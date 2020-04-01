def leapCheck(year):
 leap = False

 if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
  leap = True


 if(leap):
  print(str(year) + " is a Leap Year!")

 else:
   print(str(year) + " is not a leap year")
