# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description: Write a program that produces the following output (you must only use nested for
# loops).

def main():
    draw(6)

def draw(n):
    for i in range(1, n):
        for j in range((6 - i), 0, -1):  #figure is inversed, we need more star for upper part, so it is 6-i
            print("*", end=" ")
        print()

main()
