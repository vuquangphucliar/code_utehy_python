def giaithua(n):
    print("n = " + str(n)) #For tracking the steps
    if n == 1:
        return 1
    else:
        gt = n * giaithua(n-1)
        print("Kết quả cho ", n, " * giaithua(" ,n-1, "): ",gt) #For tracking the result by steps
        return gt

print(giaithua(10))
