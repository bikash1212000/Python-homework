# WAP to print the following patterns using  loop

# Enter number: 4
# *
# **
# ***
# ****

n = int(input("Enter Number: "))
for i in range(n+1):
   print("*"*i)

# Enter number:3
# AAA
# AA
# A

n = int(input("Enter Number: "))
for i in range(n,0,-1):
   print("A"*i)

# AAAAA
# AAAA
# AAA
# AA
# A

n = 5
for i in range(n,0,-1):
   print(" "*(n-i)+"A"*i)