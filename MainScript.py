# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:40:48 2020

@author: antho
"""

#Write a programme, which generates a random password for the user.
#Ask the user how long they want their password to be, and how many letters and numbers they want in their password.
#Have a mix of upper and lowercase letters, as well as numbers and symbols.
#The password should be a minimum of 1 characters long

import random
import numpy as np
import LengthCheck
import MinCheck
import MinofEach

#Initalisation of all the variables and list used for later
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersUpper = [x.upper() for x in letters]
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','?',',','.','/','=','%', ' ', '"', '#', '%', '*', '+', '-', ';', '@', '[',']','^','~','{','}','|']
possi = ['letters','lettersUpper', 'numbers', 'symbols']
nLet = 0
minnLet = 0
nLetMaj = 0
minnLetMaj = 0
nNum = 0
minnNum = 0
nSym = 0
minnSym = 0
#Minimum length of the password
minLength = 1
#User decide length of the password
length = LengthCheck.LengthCheck(minLength)
#User decide how much of each type he has
minOfEach = MinofEach.MinofEach(minnLet, minnLetMaj, minnNum, minnSym, length)
#minOfEach = [minnLet, minnLetMaj, minnNum, minnSym] => Reminder for debugging later

passwordFinal = [None]*length


for i in range(length) :
    choice = random.choice(possi)
    #Check if there's one of each at least
    if i >= length - (sum(minOfEach)-1) and sum(minOfEach)>1 :
        choice = MinCheck.MinCheck(nLet, nLetMaj, nNum, nSym, possi, minOfEach)
    #apply the result of random.choice
    if choice == 'letters' and minOfEach[0] > 0 :
        passwordFinal[i] = random.choice(letters)
        nLet +=1
    elif choice == 'numbers' and minOfEach[2] > 0:
        passwordFinal[i] = random.choice(numbers)
        nNum +=1
    elif choice == 'symbols' and minOfEach[3] > 0:
        passwordFinal[i] = random.choice(symbols)
        nSym +=1
    elif choice == 'lettersUpper' and minOfEach[1] > 0:
        passwordFinal[i] = random.choice(lettersUpper)
        nLetMaj +=1
    else : #Goal : solve the issue when only a few one above are choosen as a minimum
        arrayMinOfEach = np.array(minOfEach)
        arrayPossi = np.array(possi)
        arrayPossi = arrayPossi[arrayMinOfEach>0]
        choice = random.choice(arrayPossi)
        if choice == 'letters' :
            passwordFinal[i] = random.choice(letters)
            nLet +=1
        elif choice == 'numbers' :
            passwordFinal[i] = random.choice(numbers)
            nNum +=1
        elif choice == 'symbols' :
            passwordFinal[i] = random.choice(symbols)
            nSym +=1
        elif choice == 'lettersUpper' :
            passwordFinal[i] = random.choice(lettersUpper)
            nLetMaj +=1
#print the password        
print(" ".join(passwordFinal).replace(" ",""))
