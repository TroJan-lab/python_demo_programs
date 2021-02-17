import random
li=[]
guessed=[]
for i in range(0,3):
    li.append(random.randint(1,50))
def pattern(guessed):
    c=1
    for i in range(0,5):
        for j in range(0,10):
            if c not in guessed:
                print('*',end='')
            elif c in guessed:
                print('X',end='')
            c+=1
        print()
dec='true'
while dec=='true':
    in_1=int(input('enter a num : '))
    if in_1 not in guessed and in_1 not in li and in_1<=50:
        guessed.append(in_1)
    elif in_1 in guessed:
        print('please enter a unique value.')
    elif in_1 > 50 :
        print('Please enter a value less than or equal to 50.')
    if in_1 not in li:
        pattern(guessed)
    elif in_1 in li:
        dec='false'
        print('You entered a value having mine !!! ')
        print('You guessed {} times correctly.'.format(len(guessed)))

        