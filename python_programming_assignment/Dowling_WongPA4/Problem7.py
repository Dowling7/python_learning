# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description: prompts the user for a positive integer n and prints each number
# from 1 up to n, inclusive, boxed by square brackets.

def main():
    fig()

def fig():
    n = int(input("Please enter a positive integer:"))
    for i in range(n):
        print("[", i + 1, "]", end=" ")  #divide it into three parts, bracket+number+bracket

main()