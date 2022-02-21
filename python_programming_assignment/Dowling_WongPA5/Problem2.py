# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #5
#
# Description:Write a program that prompts the user to enter a positive integer value, and compute the
# following sequence:
# • If the value is even, halve it.
# • If it's odd, multiply by 3 and add 1.
# • Repeat this process until the value is 1, printing out each value.
# • Finally print out how many of these operations you performed.

def main():
    inte=int(input("Please input a positive integer to continue "))
    sum(inte)

def sum(x):#This is the whole process of calculating
    if x<1:
        print("Input error, please type an interger bigger than 1.")#if input is less than one, we should stop before process
        return
    else:
        print("Initial value is:", x)
        p = threen(x)
        print("Final value 1, number of operations performed", p-1)

def threen(n):
    if n ==1:
        return 1
    if n%2 == 0:
        n = n/2
        n=int(n)
        print("Next value is:",n)
    else:
        n = 3*n+1
        n=int(n)
        print("Next value is:",n)
    count = threen(n)+1#Get itself a auto calculating function, if n==1, stop, if n!=1 keep going
    return count

main()