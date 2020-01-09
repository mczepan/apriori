# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:37:05 2020

@author: Mario
"""

def binaryzacja(X):
    for i in range(0,len(X)):
        for j in range(0,len(X[i])):
            if(X[i][j] > 0):
                X[i][j] = 1
    return X

def supp_laczone(args):
    s = 0
    for i in range(len(args[0])):
        row = []
        for arg in args:
            row.append(arg[i])        
        if all(list(map(lambda x: x == 1,row))):
           s+=1
    return s


def supp(A):
    if (type(A[0]) != list):
        return sum(A)
    else:
        s = []
        for a in A:
            s.append(sum(a))
        return s

def zbiory_czeste(A,minSupp):
    zbiory = []
    for i in range(len(A)-1,-1,-1):
        zbior_nazwa = ''
        zbior = []
        print('A'+str(i+1),A[i])
        
        if supp(A[i])>minSupp:
            zbior.append(A[i])
            zbior_nazwa += 'A'+str(i+1)
            zbiory.append(zbior_nazwa)
            j = i+1
            while(j<len(A)):            
                print('while',zbior)
                
                if supp_laczone([zbior,A[j]])>minSupp:
                    zbior.append(A[j])
                    zbior_nazwa += 'A'+str(j+1)
                    zbiory.append(zbior_nazwa)
                    j+=1
                else:
                    break
                    
    print(zbiory)


A1 = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0]
A2 = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
A3 = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1]
A4 = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
A = [A1,A2,A3,A4]

#print(A)
#print(supp(A))
zbiory_czeste(A,6)

#print(A)
#print(supp(A))
print(supp_laczone([A2,A3]))

