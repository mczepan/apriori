# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:37:05 2020

@author: Mario
"""

def supp(A):
    s = []
    for zbior in A:
        s.append(sum(zbior))
    return s

A1 = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0]
A2 = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
A3 = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1]
A4 = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
A = [A1,A2,A3,A4]
print(A)
print(supp(A))