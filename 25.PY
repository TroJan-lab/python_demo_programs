l=[]
m=[]
sumlm=[]
lngt=int(input('enter length of both lists-'))
for i in range(0,lngt):
    n=int(input('enter element for L-'))
    l.append(n)
for j in range(0,lngt):
    n=int(input('enter element for M-'))
    m.append(n)
for k in range(0,lngt):
    s=l[k]+m[k]
    sumlm.append(s)
print('sum of corresponding elements=',sumlm)