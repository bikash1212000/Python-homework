# WAP to check whether an inputted number  is prime or not.

def prime(n):
   for i in range(2,(n//2)+1):
       if (n % i) == 0:
           return 1
   return 0
  
def main():
   n = int(input("Enter a number: "))
   if prime(n):
       print("Non Prime")
   else:
       print("Prime")
      
if __name__ == '__main__':
   main()
