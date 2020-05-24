# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:34:20 2020

@author: antho
"""
#return a list of all the minimum required (1 of each by default)
# nLet, nLetMaj, nNum, nSym
def MinofEach(minnLet, minnLetMaj, minnNum, minnSym, length) :
    minOfEach = [minnLet, minnLetMaj, minnNum, minnSym]
    minOfEachString = ['letters lowercase', 'letters uppercase', 'number(s)', 'symbol(s)']
    while True :
        Choice = input('Do you want to personnalize the minimum of each type in your password or use the default ? (d for the default and p for personnalizing your password) ')
        if Choice == 'd' or Choice == 'default' :
            minOfEach = [1,1,1,1]
            False
            return minOfEach
        elif Choice == 'p' :
            i = 0
            while i <= len(minOfEach)-1 :
                print('How many {} minimum do you want in your password ?'.format(minOfEachString[i]))
                variable = input()
                try :
                    variable=int(variable)
                    minOfEach[i] = variable
                    totOfEach = sum(minOfEach)
                    if variable < 0 : 
                        print('Natalie, just no. Do not enter a negative number.')
                    elif totOfEach > length :
                        print("Your number will make the minimum requirement {} above the maximum length of {}, please enter a number below {}".format(totOfEach,length,variable))
                    elif totOfEach == 0 and i == len(minOfEach)-1 :
                        print('You cannot have 0 everywhere. The last must be 1 at least. Let me input it for you')
                        minOfEach[i]=1
                    else :
                        i+=1
                except :
                    print('You did not enter a number')
            return minOfEach
        else :
            print ('You did not enter a good possibility')
