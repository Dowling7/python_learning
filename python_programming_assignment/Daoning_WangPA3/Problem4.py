# Daoning Wang
# COSI 10a, Fall 2021
# Programming Assignment #3
#
# Description: Write a program that prompts for two integers representing the number of rows and
# columns, and prints a grid of integers from 1 to (rows * columns) in column major order.
# For example, if the user enters 4 and 6, your program should produce the following
# output:
# 1 5 9 13 17 21
# 2 6 10 14 18 22
# 3 7 11 15 19 23
# 4 8 12 16 20 24

def main():
    Prob4()

def Prob4():
    for i in range(1, 5): #we have 4 lines
        for j in range(6): #and 6 columns
            p = i + 4 * j #each number in one line increse by 4
            print(p, end="\t")
        print()

main()
