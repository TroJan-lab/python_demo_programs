import mysql.connector as sqlctr
import sys
hst = str(input('Enter host name/address-'))
usr = str(input('Enter user name-'))
pswd = str(input('Enter password for user '+usr+'-'))
mycon = sqlctr.connect(host=hst, user=usr, password=pswd)
if mycon.is_connected():
    print('\n')
    print('Successfully connected to '+hst)
else:
    print('Error while connecting to '+hst)
cursor = mycon.cursor()
cursor.execute('show databases')
data=cursor.fetchall()
for i in data:
    print (i)
dec=input('select database : ')
cursor.execute('use {}'.format(dec))
cursor.execute('show tables')
data=cursor.fetchall()
for i in data:
    print (i)
def update():
    tname = str(input('enter table name for updating its data-'))
    li = []
    st = 'desc '+tname
    cursor.execute(st)
    data = cursor.fetchall()
    for i in data:
        li.append(i[0])
    flag = 'true'
    while flag == 'true':
        cursor.execute('select * from {}'.format(tname))
        print('ALL DATA FROM TABLE '+tname+' ARE\n')
        data = cursor.fetchall()
        for i in data:
            print(i)
        print('\n columns in table '+tname+' are')
        print(li)
        col1 = str(input('enter column name for modification from above list-'))
        pre_value = str(
            input('enter value(present) to be changed from above data-'))
        post_value = str(input('enter new value-'))
        st = str('update %s set %s=%s where %s=%s') % (
            tname, col1, "'%s'", col1, "'%s'") % (post_value, pre_value)
        cursor.execute(st)
        cursor.execute('select * from {}'.format(tname))
        print('ALL DATA FROM TABLE '+tname+' ARE\n')
        data = cursor.fetchall()
        for i in data:
            print(i)
        print('\nVALUE UPDATED SUCCESSFULLY')
        dec = str(input('Do you want to change more data?(Y/N)-'))
        if dec == 'y' or dec == 'Y':
            flag = 'true'
        else:
            flag = 'false'
            mycon.commit()
update()