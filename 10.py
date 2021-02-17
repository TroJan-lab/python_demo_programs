f=open('D://test.txt','r')
lines=f.readlines()
for line in lines:
    x=line.split()
    for y in x:
        print(y+'#',end='')
    print('')