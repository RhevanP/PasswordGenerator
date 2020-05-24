# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:42:17 2020

@author: antho
"""
import random
# Forcing a choice if the minimum is not met
#    minOfEach = [minnLet, minnLetMaj, minnNum, minnSym]
def MinCheck(nLet, nLetMaj, nNum, nSym, possi, minOfEach) :
    if nLet < minOfEach[0] :
        return 'letters'
    elif nNum < minOfEach[2] :
        return 'numbers'
    elif nSym < minOfEach[3] :
        return 'symbols'
    elif nLetMaj < minOfEach[1] :
        return 'lettersUpper'
    else :
        return random.choice(possi)