import csv
c=0
with open('D://given_csv.csv','r') as csvfile:
    myreader=csv.reader(csvfile,delimiter=',')
    with open('D://stud_name.txt','w') as textfile:
        for row in myreader:
            c+=1
            textfile.write('{}.{}'.format(c,row[0]))
            textfile.write('\n')
        print('{} records added successfully.'.format(c))
csvfile.close()        

