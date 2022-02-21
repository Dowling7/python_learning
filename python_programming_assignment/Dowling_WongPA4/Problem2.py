# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description:Write a program that produces the following output (you must only use nested for
# loops).

def main():
    draw(6)

def draw(n):
    for i in range(1, n):
        for j in range(i):    #the number of satrs equals to the line number
            print("*", end=" ")
        print()

main()
