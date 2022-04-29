# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 20:37:28 2022

@author: Jambo
"""
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1,2,3,4]))


def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:]) 
    

def itemCount(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + itemCount(arr[1:])
    

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
            