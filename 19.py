import mysql.connector as sqlctr
mycon=sqlctr.connect(host='localhost',user='root',password='password',db='ram')
cursor=mycon.cursor()
cursor.execute('select * from books')
data=cursor.fetchall()
dec='y'
while dec.lower()=='y':
    ch=int(input('Enter serial number of book : '))
    found='false'
    for i in data:
        if int(i[0])==ch:
            print(i)
            found='true'
    if found=='false':
        print('record not found.')
    dec=input('Do you want to search more?(y/n) : ')
mycon.commit()
mycon.close()