# WAP to print first n Fibonacci numbers. 

n = int(input("Enter the number: "))
a = 0
c = 0
b = 1
while n > 0:
   print(a,end=' ')
   c = a+b
   a = b
   b = c
   n -= 1