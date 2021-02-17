def empty(li):
    if len(li)==0:
        return True
    else:
        return False
def push(li,val):
    li.append(val)
def pop(li):
    if empty(li):
        return 'UNDERFLOW'
    else:
        top=len(li)-1
        val=li.pop(top)
        if len(li)==0:
            top=None
        else:
            top=len(li)-1
        return val
li=[]
top=None
while True:
    print('''
Enter 1 : To Push
Enter 2 : To Pop
Enter 3 : To Exit''')
    ch=input('enter your choice : ')
    if ch=='1':
        val=int(input('Enter value to push : '))
        push(li,val)
    elif ch=='2':
        val=pop(li)
        if val=='UNDERFLOW':
            print('stack is empty')
        else:
            print('value poped successfully')
    else:
        break
