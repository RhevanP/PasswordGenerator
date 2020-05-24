# -*- coding: utf-8 -*-
"""
Created on Fri May 22 20:56:53 2020

@author: antho
"""

def LengthCheck(minLength) :
    #Check what is the length the user wants
    while True :
        length = input("How long do you want your password to be? ")
        try :
            lengthChecked = int(length)
            if lengthChecked < 0 :
                print('You cannot enter a negative value for a length...')
            elif lengthChecked >= minLength :
                return lengthChecked
                False
            else :
                print("Your number is below the minimum accepted (which is {}). Try again.".format(minLength))
        except :
            print("Please enter a valid number above 6")