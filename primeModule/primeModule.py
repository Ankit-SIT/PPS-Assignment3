
def Check(number):
 if(number > 1):
    for i in range(2,number//2):
         if(number % i) == 0:
             print("Number is not a Prime!")
             break
         else:
             print("Number is a Prime!")
             break
 else:
    print("Number is not a Prime!")
