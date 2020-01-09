# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:37:05 2020

@author: Mario
"""

def supp(A,B,*args):
    return sum(A,B)


def supp(A):
    return sum(A)

def zbiory_czeste(A,minSupp):
    for i in range(len(A)-1,-1,-1):
        print('A'+str(i+1),A[i])
        if supp(A[i])>minSupp:
            print('asda')
#        j = i
#        while j>0:
#            print('A',str(j),":",supp(A[j-1]))
#            j-=1


A1 = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0]
A2 = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
A3 = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1]
A4 = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
A = [A1,A2,A3,A4]
#print(A)
#print(supp(A))
zbiory_czeste(A,6)