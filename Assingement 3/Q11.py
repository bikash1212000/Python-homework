# WAP to print the following patterns using  loop

#    O
#   OOO
#  OOOOO
# OOOOOOO

for i in range(4):
   for j in range(7):
       if j >= 3-i and j <= 3+i:
           print("O",end="")
       else:
           print(" ",end="")
   print()

# OOOOOOO
#  OOOOO
#   OOO
#    O

for i in range(4):
    for j in range(7):
       if j >= i and j <= 6-i:
           print("O",end="")
       else:
           print(" ",end="")
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = 4
count = 1
for i in range(n+1):
   for _ in range(i):
       print(count,end=' ')
       count += 1
   print()