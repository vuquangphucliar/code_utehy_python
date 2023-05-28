def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
def reduced_fraction(numerator,demominator):
    sign=numerator*demominator
    sign=sign/abs(sign)
    numerator=abs(numerator)
    demominator=abs(demominator)
    return sign*numerator/gcd(numerator,demominator),demominator/gcd(numerator,demominator)
print(reduced_fraction(21,14))