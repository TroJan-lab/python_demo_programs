import mysql.connector as sqlctr
mycon=sqlctr.connect(host='localhost',user='root',password='password',db='ram')
cursor=mycon.cursor()
cursor.execute('select * from books')
data=cursor.fetchall()
for i in data:
    print(i)
mycon.close()