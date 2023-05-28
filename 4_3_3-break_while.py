#Checking the prime number
n=int(input('Input an integer number:'))
i=2;                #Try to divide with two first,
ok=True;
while i<n/2:        #Test with the half of n
    if n%i==0:      #if n divisibility with every numbers,
        ok=False;       # n is not a prime number
        break           #break and then show notification
    i+=1            #Check with next value of i
if ok:
   print(n,' is a prime number.')
else:
   print(n, ' is not a prime number.')
