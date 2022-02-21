# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #7
#
# Description:Write a function called collapse that accepts a list of integers as a parameter and
# returns a new list containing the result of replacing each pair of integers with the sum of that pair.
# For example, is a list called list1 stores the values [7, 2, 8, 9, 4, 13, 7, 1, 9,
# 10], then the call of collapse(list1) should return a new list containing [9, 17, 17,
# 8, 19]. The first pair of the original list is collapsed into 9 (7+2), the second pair is collapsed
# into 17 (8+9), etc. If the list store an odd number of elements, the final elements is not collapsed.
# For example, if the list had been [1, 2, 3, 4, 5], then the call would return [3, 7, 5].
# Your function should not change the list that is passed as a parameter.

import math
def main():
    list1=[7, 2, 8, 9, 4, 13, 7, 1, 9, 10]
    list2=[1, 2, 3, 4, 5]
    collapse(list1)
    collapse(list2)

def collapse(lis):
    if len(lis)%2==1:
        lis[len(lis):] = [0]
    neolis=[0]*int(math.ceil(len(lis)/2))    #so that for odd number, index will not out of range
    i=0
    for j in range (0, len(lis), 2):
        neolis[i]=lis[j]+lis[j+1]    #i and j are separated and counted, it works more clearly for two lists
        i+=1
    return neolis
main()