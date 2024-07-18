# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 07:24:04 2022

"""
def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)
        
        
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
