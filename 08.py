print('''choose which function to use:
1. Square root (sqrt)
2. Factorial
3. Power
4. Log
Trigonometric functions:
5. sin
6. cos
7. tan
Values of constants:
8. e
9. pi
10. tau''')
x=int(input('enter operation number : '))
e=2.718281828459045
pi=3.141592653589793
tau=6.283185307179586
import math
if x==1:
    a=int(input('enter a number:'))
    print(math.sqrt(a))
elif x==2:
    a=int(input('enter a number:'))
    f=a
    for i in range(a-1,0,-1):
        f=f*i
    print(f)
elif x==3:
    a=int(input('enter a number : '))
    b=int(input('enter power : '))
    print(math.pow(a,b))
elif x==4:
    a=int(input('enter a number : '))
    b=int(input('enter base : '))
    print(math.log(a,b))
elif x==5:
    angle=int(input('enter angle in degrees : '))
    angle_new=(3.14/180)*angle
    print(math.sin(angle_new))
elif x==6:
    angle=int(input('enter angle in degrees : '))
    angle_new=(3.14/180)*angle
    print(math.cos(angle_new))
elif x==7:
    angle=int(input('enter angle in degrees : '))
    angle_new=(3.14/180)*angle
    print(math.tan(angle_new))
elif x==8:
    print(e)
elif x==9:
    print(pi)
elif x==10:
    print(tau)
else:
    print('please enter a valid operation number.')