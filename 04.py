def main(tup):
    e,o=0,0
    for i in range(0,len(tup)):
        if tup[i]==0:
            pass
        elif (tup[i]%2)==0:
            e+=1
        else:
            o+=1
    print('number of even number : ',e,'number of odd number',o)
tup=eval(input('enter a tuple'))   
main(tup)     