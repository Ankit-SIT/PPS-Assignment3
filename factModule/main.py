#!/usr/bin/python3

import factModule

print("Enter a Number: ")
number = int(input())

print("Factorial of " + str(number) + " is "+ str(factModule.fact(number)))
