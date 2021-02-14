# WAP to display factors of an inputted  number.

n = int(input("Enter a number to find its factor: "))
if n == 0:
   print(1)
else:
   f = ""
   for i in range(1,n+1): 
       if n % i == 0:
           f += str(i)+" "
   print("Factors of ",n,":",f,end=" ") 
