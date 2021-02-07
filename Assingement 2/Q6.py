# WAP to input a number and  check whether the number is  divisible by 5 and 3 or not.
import re
n = input("Enter a number: ")
 
if re.match('^[+-]?([0-9]*[.])?[0-9]+$',n):
   n = float(n)
   if n % 3 == 0 and n % 5 == 0:
       print("The given number is divisible by 3 and 5")
   else:
       print("The given number is not divisible by 3 and 5")
else:
   print("please enter valid input")
