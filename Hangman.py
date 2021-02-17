print("\n\n______WELCOME TO HANGMAN______")
print(
'''
   _ _ _ _
   |/  |
   |   O
   |./ | \.
   | _/ \_
   |
(- - - )


''')
word='PYTHON'
li_guessed=[]
wrong_letters=[]
def letters(li_guessed):
    print('word  : ',end='')
    for i in word:
        if i in li_guessed:
            print(i,end=' ')
        else:
            print('_ ',end=' ')
letters(li_guessed)
while len(li_guessed)<(len(word)):
    in_1=(input('\nenter a letter : '))
    in_1=in_1.upper()
    if (in_1 in word) and (in_1 not in li_guessed) and (in_1!='') :
        li_guessed.append(in_1.upper())
    else:
        if in_1!='' and in_1 not in li_guessed and in_1 not in wrong_letters:
            wrong_letters.append(in_1.upper())
        else:
            pass
    letters(li_guessed)
print()
print(li_guessed)
print(wrong_letters)
print('Total distinct attempt : ',(len(li_guessed)+len(wrong_letters)))
print('Correct attempt : ',len(li_guessed))
print('Wrong attempt : ',len(wrong_letters))