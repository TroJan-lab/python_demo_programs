import pickle
sdata={}
totals=int(input("Enter number of students :"))
a=open ('D://txt14.txt','wb')
for i in range (totals):
    sdata["Roll no"]=int (input("Enter roll no. : "))
    sdata["Name"]=input("Enter name : ")
    sdata["Marks"]=float(input("Enter marks : "))
    pickle. dump (sdata, a)
    sdata={}
a.close()
found=False
rollno=int (input("Enter roll number of student with wrong entry : "))
a=open('D://txt14.txt','rb+')
try:
    while True:
        pos=a.tell()
        sdata=pickle.load(a)
        if (sdata['Roll no']==rollno):
            sdata['Marks']=float(input('Enter new marks : '))
            a.seek(pos)
            pickle.dump(sdata,a)
            found=True
except EOFError:
    if found==False:
        print('roll number not found.')
    else:
        print('Students marks updated successfully.')
    a.close()