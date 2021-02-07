# WAP to input marks of 5  subject and find average and  assign grade. 
# Average Marks   Grade
# 90 & above        O 
# 80 – 89           E 
# 70-79             A 
# Below 70          B

import re
s1, s2, s3, s4, s5 = input("Enter the marks of five subjects: ").split()
 
if  (re.match('^[+]?([0-9]*[.])?[0-9]+$',s1) and
   re.match('^[+]?([0-9]*[.])?[0-9]+$',s2) and
   re.match('^[+]?([0-9]*[.])?[0-9]+$',s3) and
   re.match('^[+]?([0-9]*[.])?[0-9]+$',s4) and
   re.match('^[+]?([0-9]*[.])?[0-9]+$',s5)):
 
   s1 = float(s1); s2 = float(s2); s3 = float(s3)
   s4 = float(s4); s5 = float(s5)
   avg = (s1+s2+s3+s4+s5)/5
   if avg >= 90:
       print("Grade is O")
   elif avg >= 80:
       print("Grade is E")
   elif avg >= 70:
       print("Grade is A")
   else:
       print("Grade is B")
else:
   print("please enter valid input")
