wt=['Rain','Light rain','Sunny','Fog','Fog-Rain','ThunderStorm']
wt_Rain_found=[]
st=input('Nhap vao loai thoi tiet ban muon tim: ')
for i in wt:
    if i.find(st)>=0:
        wt_Rain_found.append(i)
print(wt_Rain_found)
