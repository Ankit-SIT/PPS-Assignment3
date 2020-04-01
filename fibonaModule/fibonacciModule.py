

def fibonacci(n):
 first = 0
 second  = 1


 print(first)
 print(second)

 for counter in range(1,n-1):
   third =  second + first
   first = second
   second = third
   print(third)
