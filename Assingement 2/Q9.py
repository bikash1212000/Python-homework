a=int(input("Enter 2 digit number:"))
r=0
while(a>0):
    b=a%10
    r=(r*10)+b
    a=a//10
print("Reverse of the given number is: ",r)
