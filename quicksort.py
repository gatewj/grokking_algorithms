# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 20:53:53 2022

@author: Jambo
"""
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10,5,2,3]))