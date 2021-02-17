file=open('D://test.txt','r')
lines=file.readlines()
file.close()
file=open('D://test.txt','w')
file1=open('D://test2.txt','w')
for line in lines:
    if 'a' in line:
        file1.write(line)
    else:
        file.write(line)
print('lines that contain a character are removed from test.txt')
print('lines that contain a character are added in test2.txt')
file.close()
file1.close()