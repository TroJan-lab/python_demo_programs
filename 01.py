li=[]
global c
c=0
len_li=int(input('Enter length of list : '))
for i in range(0,len_li):
    val=float(input('enter a number : '))
    li.append(val)
print('Given list : ',li)
item_search=float(input('enter number to be searched : '))
for j in range(0,len_li):
    if li[j]==item_search:
        print('item found at index ',j)
        c=c+1
print('frequency of given item : ',c)