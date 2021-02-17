import csv
with open('D://employee.csv','w')as csvfile:
    mywriter = csv.writer (csvfile, delimiter=',')
    ans='y'
    while ans.lower()=='y':
        eno=int (input("Enter Employee ID: "))
        name=input("Entar Employee Name :")
        mobno=int(input ("Enter Employee Mobile No :"))
        mywriter.writerow([eno, name, mobno])
        ans=input('Do You Want To Enter More Data?(Y/N)')
with open('D://employee.csv','r') as csvfile:
    ans='y'
    while ans.lower()=='y':
        found='False'
        myreader = csv.reader (csvfile, delimiter=',')
        e = int(input("Enter Employee ID to search : "))
        csvfile.seek(0)
        for row in myreader:
            if len(row)>0:
                if int(row[0])==e:
                    print('Record found.')
                    print('Name : ',row[1])
                    print('Contacts : ',row[2])
                    found='True'
        if found=='False':
            print('No Records found.')
        ans=input('Do you want to search more records(y/n) : ')
        if ans.lower()=='y':
            pass
        elif ans.lower()!='y':
            break        
