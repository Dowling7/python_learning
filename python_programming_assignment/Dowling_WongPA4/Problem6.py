# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description: Modify the program for problem 5 to make use of a constant for the height
# of the figure. Program should output a figure of height 4.

def main():
    draw(4)

def draw(n):
    for i in range(n):
        print("\\\\" * i + "!" * ((4 * n - 2) - 4 * i) + "//" * i) #the same as last program

main()