# Write a program to accept a  character from the user and  display whether it is a vowel or  consonant.
import re
ch = input("Enter a character: ")
if re.match('^[a-z]+$',ch, re.I):
   if len(ch) == 1:
       if re.match('^[aeiou]+$',ch, re.I):
           print(ch,"is a vowel")
       else:
            print(ch,"is a consonant")
   else:
       print("Enter only one char")
else:
   print("please enter valid input")
