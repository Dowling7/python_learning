# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description: Write a program that produces the following output (you must only use nested for
# # loops).

def main():
    draw(6)

def draw(n):
    for i in range(n-1,0,-1):
        for j in range(i):
            print(" ", end=" ")  #In this case, space need to be taken into account
        for j in range(6-i):
            print("*",end=" ")
        print()

main()