def count_vowel(str):
    c=0
    li=['A','E','I','O','U']
    for i in range(0,len(str)):
        if str[i].upper() in li:
            c+=1
    return c
str=input('enter a string : ')
print('vowels in given str : ',count_vowel(str))