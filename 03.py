def main(li):
    for i in range(0,len(li)):
        if li[i]==0:
            pass
        elif (li[i]%2)==0:
            li[i]/=2
        else:
            li[i]*=2
    print('list after modification : ',li)
lst=eval(input('enter a list : '))    
main(lst)        
