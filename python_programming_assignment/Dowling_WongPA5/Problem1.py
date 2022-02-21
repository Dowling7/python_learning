# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #5
#
# Description:Write a program that prompts the user to enter numbers, then print the smallest and largest of all
# numbers supplied by the user

def main():
    n=int(input("How many numbers do you want to enter?"))
    sort(n)

def sort(n):
    for i in range(1):
        d=str(i+1)
        a=b=float(input("Number "+d+": "))
    for i in range(2,n+1):
        d=str(i)
        c=float(input("Number "+d+": "))
        if c>a:#substitue, if we got a smaller one, then it becomes the new smallest number
            a=c
        if c<b:
            b=c
        a=int(a)#we are asked to print integer for the final result
        b=int(b)
    print("Smallest=",b)
    print("Largest=",a)

main()
