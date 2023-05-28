stack=[]
tp=[10,11,12,13,14,15,16]
tlp=['A','B','C','D','E','F']
A=195
X=2
while A!=0:
    r=A%X
    A=A//X
    stack.append(r)
while stack!=[]:
    a=stack.pop()
    if a>=10:
        for i in range(len(tp)):
            if a==tp[i]:
                a=tlp[i]
    print(a,end='\t')
