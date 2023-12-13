
from os import system , name
def clear():
	if name=='nt':
		_= system('cls')
	else:
		_ = system ('clear')
print("welcome to guesses PYTHON CODING WORD")
import random as ra
name=input("enter your name? ")
print('good luck',name)
while True:
    word=['python','not','open','end','break','try','True','list','tuple','for','range''dict','key','values','cmp','items','setdefaultkey','print','str','string','tuple'
          ,'elif','else','break','while','True','eval','int','input','tkinter','button','and','append','extend','notin','not','pop','remove','count','max','min','sum',
          'python','not','open','end','break','try','True','list','tuple','for','range''dict','key','values','cmp','items','setdefaultkey','print','str','string','tuple'
          ,'elif','else','break','while','True','eval','int','input','tkinter','button','and','append','extend','notin','not','pop','remove','count','max','min','sum',
          'python','not','open','end','break','try','True','list','tuple','for','range''dict','key','values','cmp','items','setdefaultkey','print','str','string','tuple'
          ,'elif','else','break','while','True','eval','int','input','tkinter','button','and','append','extend','notin','not','pop','remove','count','max','min','sum']
    word=ra.choice(word)
    print("Guess the characters")
    guess=''
    guess+=word[0]
    guess+=word[len(word)-1]
    turns=12
    while turns>0:
        failed=0
        for char in word:
            if char in guess:
                print(char)
            else:
                print("_")
                failed+=1
        if failed==0:
            print('you win')
            print('the word is : ',word,"""

""")
            break
        gues=input('guess a character:')
        if len(gues)>=2:
                print("you can only enter one letter")
                break
        guess+=gues
        if gues not in word:
            turns-=1
            print('wrong')
            print('you have',turns,'more guesses')
        if turns==0:
            print('you loose')
a=input()
