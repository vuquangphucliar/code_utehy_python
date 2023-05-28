#Input integer numbers n and k, n>=k and k>0
while(True):
    n=int(input('Enter number n: '))
    k = int(input('Enter number k: '))
    if (n>=k) and (k>0):
        break
#Calculate the factorial of n
factorial_n=1
for i in range(1,n+1):
    factorial_n=factorial_n*i
#Calculate the factorial of k
factorial_k=1
for i in range(1,k+1):
    factorial_k=factorial_k*i
#Calculate the factorial of (n-k)
factorial_n_k=1
for i in range(1,n-k+1):
    factorial_n_k=factorial_n_k*i
Combination_n_k=factorial_n/(factorial_k*factorial_n_k)
print(Combination_n_k)
