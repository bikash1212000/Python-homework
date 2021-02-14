# WAP to calculate and display the factorial of  an inputted number.

n = int(input("Enter the number: "))
if n < 0:
   print("Factorial is defined only for  non negative number")
elif n == 0:
   print("The factorial of",n,"is",0)
else:
   factorial = 1
   for i in range(1,n+1): 
       factorial = factorial*i 
   print("The factorial of",n,"is",factorial)