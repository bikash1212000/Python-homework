# WAP to calculate sum of first n numbers. 1+2+…+n

n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1): 
   sum += i
print("sum of first",n,"numbers :",sum) 