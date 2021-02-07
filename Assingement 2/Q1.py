# WAP to determine a student’s  final grade and indicate whether  they are passing or failing. The  final grade is calculated as the  average of marks of four  
# subjects.

import re
s1 = input("Enter marks of subject 1: ")
s2 = input("Enter marks of subject 2: ")
s3 = input("Enter marks of subject 3: ")
s4 = input("Enter marks of subject 4: ")

if (re.match('^[+-]?([0-9]*[.])?[0-9]+$',s1) 
    and re.match('^[+-]?([0-9]*[.])?[0-9]+$',s2)
    and re.match('^[+-]?([0-9]*[.])?[0-9]+$',s3) 
    and re.match('^[+-]?([0-9]*[.])?[0-9]+$',s4)):

    s1 = float(s1); s2 = float(s2); s3 = float(s3); s4 = float(s4)
    avg = (s1+s2+s3+s4)/4

    print("Your Grade is: ",avg)
    if avg >= 40:
        print("Congratulation You have Passed")
    else:
        print("Sorry You Failed")
else:
    print("please enter valid input")