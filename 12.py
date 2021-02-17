print("ENTER ~ to exit")
f1=open('D://lower.txt','w')
f2=open('D://upper.txt','w')
f3=open('D://other.txt','w')
while True:
    c=input('enter a single character : ')
    if c=='~':
        break
    elif c.islower():
        f1.write(c)
    elif c.isupper():
        f2.write(c)
    else:
        f3.write(c)
f1.close()
f2.close()
f3.close()
