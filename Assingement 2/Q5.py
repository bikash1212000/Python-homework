# WAP to input a number and  check whether the number is 2  digit number or not.
import re
n = input("Enter a number ")
 
if re.match('^[+-]?([0-9]*[.])?[0-9]+$',n):
   if len(n)==2:
       print("the given number is two digit number")
   else:
       print("The given number is not two digit")
else:
   print("please enter valid input")
