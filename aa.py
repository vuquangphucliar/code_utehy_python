# MH=[["12001","Sua chua VN",100,5000],["15003","Sua bot 400gV",0,90000],["XP01","Xa phong O 1kg",20,32000]]
# print(MH)
# for i in range(0,len(MH)-1):
#     for j in range(i+1,len(MH)):
#         if MH[i][3]<MH[j][3]:
#             K=MH[i]
#             MH[i]=MH[j]
#             MH[j]=K
# print(MH)
L=[256,128,64,32,16,8,4,2,22,1]
A=257
for i in range(len(L)):
    if A>=L[i]:
        r=1
        A = A - L[i]
    else:
        r=0
    print(r,end='\t')