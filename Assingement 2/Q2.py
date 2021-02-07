# WAP to find the largest number  between two inputted numbers.
import re
n1 = input("Enter first number: ")
n2 = input("Enter first number: ")
 
if (re.match('^[+-]?([0-9]*[.])?[0-9]+$',n1)
   and re.match('^[+-]?([0-9]*[.])?[0-9]+$',n2)):
   n1 = float(n1); n2 = float(n2)
   if n1 > n2:
       print("First number is largest")
   elif n2 > n1:
       print("Second number is largest")
   else:
       print("Both are equal")
else:
    print("please enter valid input")