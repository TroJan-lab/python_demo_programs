global dic
dic={}
def create_dict(n):
    for i in range(0,n):
        key=input('enter key : ')
        value=input('enter value : ')
        dic[key]=value
def val_changer(k,v):
    dic[k]=v
n=int(input('enter no. of keys required : '))
create_dict(n)
print('Given_dictionary : ',dic)
print(dic.keys())
dec=input('enter key name for modification from above list : ')
val=input('enter value for updation : ')
val_changer(dec,val)
print('Dictionary with updated value : ', dic)