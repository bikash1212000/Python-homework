# WAP to input 3 side of a  
# triangle and prints its type (i.e  Equilateral/Isosceles/Scalene).
import re
x, y, z = input("Enter the length of three side of the triangle: ").split()
 
if (re.match('^[+]?([0-9]*[.])?[0-9]+$',x) and
   re.match('^[+]?([0-9]*[.])?[0-9]+$',y) and
   re.match('^[+]?([0-9]*[.])?[0-9]+$',z)):
   if x==y==z:
       print("Equilateral")
   elif x==z or y==z or x==y:
       print("Isosceles")
   else:
       print("Scalene")
else:
     print("please enter valid input")