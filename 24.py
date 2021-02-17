li=[]
li1=[]
n=int(input('enter length of list-'))
for i in range(0,n):
    el=float(input('enter number-'))
    li.append(el)
for m in li:
    if m not in li1:
        li1.append(m)
print('original list-',li)
print('list after removing dublicates-',li1)