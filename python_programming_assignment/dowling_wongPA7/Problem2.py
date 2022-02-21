# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #7
#
# Description:Write a function called is_sorted that accepts a list of numbers as a parameter
# and return True if the list is sorted (nondecreasing) order and False otherwise. For example, if
# lists named list1 and list2 store [16.1, 12.3, 22.2, 14.4] and [1.5, 4.3,
# 7.0, 19.5, 25.1, 46.2], respectively, the calls is_sorted(list1) and
# is_sorted(list2) should return False and True, respectively. Assume the list has at
# least one element. A one-element list is considered to be sorted.

def main():
    list1=[16.1, 12.3, 22.2, 14.4]
    list2=[1.5, 4.3, 7.0, 19.5, 25.1, 46.2]
    is_sorted(list1)
    is_sorted(list2)
    
def is_sorted(lis):
    flag = 0
    i = 1
    while i < len(lis):
        if(lis[i] < lis[i - 1]):
            flag = 1
        i += 1
    if (not flag) :         #If one element is not sorted, flag will have value, if flag is still 0, then the list is sorted.
        return True
    else :
        return False
        
main()
