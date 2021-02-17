import mysql.connector as sqlctr
mycon=sqlctr.connect(host='localhost',user='root',password='password',db='ram')
cursor=mycon.cursor()
ch1=int(input('Enter serial number : '))
cursor.execute('select * from books where SN = {}'.format(ch1))
data=cursor.fetchall()
for i in data:
    print(i)
ch=input('Do you want delete this record?(y/n) : ')
if ch.lower()=='y':
    cursor.execute('delete from books where SN = {}'.format(ch1))
    print('data deleted successfully.')
else:
    pass
mycon.commit()
mycon.close()