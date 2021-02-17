import mysql.connector as sqlctr
mycon=sqlctr.connect(host='localhost',user='root',password='password',db='ram')
cursor=mycon.cursor()
ch1=int(input('Enter serial number : '))
cursor.execute('select * from books where SN = {}'.format(ch1))
data=cursor.fetchall()
for i in data:
    print('data before updation : \n',i)
ch=int(input('Enter new value for Quantity_available : '))
cursor.execute('update books set Quantity_Available= "{}" where SN = {}'.format(ch,ch1))
cursor.execute('select * from books where SN = {}'.format(ch1))
data=cursor.fetchall()
for i in data:
    print('data after updation : \n',i)
mycon.commit()
mycon.close()