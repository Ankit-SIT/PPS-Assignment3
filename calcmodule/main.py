#!/usr/bin/python3

import calcmodule

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("ENTER YOUR CHOICE: ",end='')
choice = int(input())

if(choice > 4):
     exit(-1)

print("ENTER THE TWO OPERANDS: ")
print("a = ",end='')
a = int(input())
print("b = ",end='')
b = int(input())

if(choice == 1):
     result = calcmodule.add(a,b)

elif(choice == 2):
     result = calcmodule.sub(a,b)

elif(choice == 3):
     result = calcmodule.mul(a,b)

elif(choice == 4):
     result = calcmodule.div(a,b)
     


print("RESULT IS :" + str(result))
