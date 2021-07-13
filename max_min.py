import math
import os
import random
import re
import sys


def maxMin(k, arr):  #Python solution
    i=-1
    j=k-2
    arr.sort()#   arr=[1,2,3,4,5,6,7,8,9,10]
    m=arr[-1]
    while(j<len(arr)-1):
        
        i+=1
        j+=1
        min_arr=arr[i]
        max_arr=arr[j]
        m=min(m,max_arr-min_arr)
        
    return m
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
