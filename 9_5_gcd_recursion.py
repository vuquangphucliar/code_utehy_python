
#GCD - Greatest Common divisor - Ước số chung lớn nhất
#LCM - Lowest Common Multiple - Bội số chung lớn nhất

#Calculate GCD by using recursion
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
a=24
b=15
print(f'{a}/{b}={a/gcd(a,b)}/{b/gcd(a,b)}')


