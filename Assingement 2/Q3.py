# WAP that reads two numbers  and an arithmetic operator and  displays the result.
import re
a = input("Enter first number: ")
b = input("Enter second number: ")
op = input("Enter operator: ")
 
if (re.match('^[+-]?([0-9]*[.])?[0-9]+$',a)
   and re.match('^[+-]?([0-9]*[.])?[0-9]+$',b)):
   a = float(a)
   b = float(b)
   if op == '+':
       print("Result: ",a+b)
   elif op == '-':
       print("Result: ",a-b)
   elif op == '/':
       if b == 0:
           print("we cannot divide any number by 0")
       else:
           print("Result: ",a/b)
   elif op == '*':
       print("Result: ",a*b)
   else:
       print("invalid operator")
else:
   print("please enter valid input")
