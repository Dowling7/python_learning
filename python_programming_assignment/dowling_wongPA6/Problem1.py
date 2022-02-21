# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #6
#
# Description: You must use while loops. Write a program that prompts the user to enter a positive integer
#value, and compute the following sequence:
#• If the value is even, halve it.
#• If it's odd, multiply by 3 and add 1.
#• Repeat this process until the value is 1, printing out each value.
#• Finally print out how many of these operations you performed.
#Note: If the input value is less than 1, print a message containing the word Error and exit the
#program. You can assume that the input will have smaller than 200 operations.

def main():
    num=int(input("Please input a positive interger bigger than 1: "))
    cont=threen(num)
    print("Final value 1, number of operations performed",cont+1)



def threen(x):
    print("Initial value is",x )
    count=0
    if x<1:
        print("Error, please input a number bigger than 1.")
        return 0
    while x>2:
        if x%2==0:
            x=x/2
            x=int(x)
            print("Next value is:",x)
            count+=1
        else:
            x=x*3+1
            x=int(x)
            print("Next value is:",x)
            count+=1
    return count      

main()