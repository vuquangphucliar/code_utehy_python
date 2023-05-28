#Nhập vào hai số n và k, n>=k và k>0
def giaithua(x):
    giaithua = 1
    for i in range(1,x+1):
        giaithua = giaithua * i
    return giaithua

while(True):
    n=int(input('Nhập vào số n: '))
    k = int(input('Nhập vào số k: '))
    if (n>=k) and (k>0):
        break
#Tính tổ hợp chập k của n C(n,k)
tohopchap_n_k=giaithua(n)/(giaithua(k)*giaithua(n-k))
print(tohopchap_n_k)
