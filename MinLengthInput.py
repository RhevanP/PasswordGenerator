# -*- coding: utf-8 -*-
"""
Created on Sun May 24 09:42:05 2020

@author: antho
"""

def MinLengthInput() :
    #User Input the minimum length he wants in his password
    while True :
        minInput = input('What is the minimum length you want ?')
        try :
            minInputCh = int(minInput)
            if minInputCh < 0 :
                print('You cannot have a negative length')
            elif minInputCh == 0 :
                print('Your minimum length must be at least 1')
            else :
                return minInputCh
        except :
            print('You did not enter a number')