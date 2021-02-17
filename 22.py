file=open('D://t22.txt','r')
content=file.read()
max=0
max_occuring_word=''
occurences_dict={}
words=content.split()
for word in words:
    count=content.count(word)
    occurences_dict.update({word:count})
    if (count>max):
        max=count
        max_occuring_word=word
print('Most occuring word is ',max_occuring_word)
print('No. of times it is occuring : ',max)
print('Frequency of other word is : ')
print(occurences_dict)