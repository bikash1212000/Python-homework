# WAP to display all the prime number upto n. 

n = int(input("Enter the number:  "))
print("Prime numbers: ",end="")
for j in range(2,n+1):
   f = 0
   for i in range(2,(j//2)+1):
       if (j % i) == 0:
           f = 1
           break
   if f == 0:
       print(j,end = ' ')