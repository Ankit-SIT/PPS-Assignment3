

def divisor(grade):
 if((grade == 'A') or (grade == 'a')):
     division = 'A'

 elif((grade == 'B') or (grade == 'b')):
     division = 'B'

 elif((grade == 'C') or (grade == 'c')):
      division = 'C'

 else:
      print("FAILED CLASS!")
      exit(0)

 print("Division is : " + str(division))
