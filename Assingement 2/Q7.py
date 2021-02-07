# WAP to input 3 numbers and  find the second smallest.
import re
x, y, z = input("Enter three numbers: ").split()
 
if  (re.match('^[+-]?([0-9]*[.])?[0-9]+$',x) and
   re.match('^[+-]?([0-9]*[.])?[0-9]+$',y) and
   re.match('^[+-]?([0-9]*[.])?[0-9]+$',z)):
 
   if x<y<z or z<y<x:
       print(y,"is the second smallest")
   elif y<z<x or x<z<y:
       print(z,"is the second smallest")
   else:
       print(x,"is the second smallest")
 
else:
   print("please enter valid input")