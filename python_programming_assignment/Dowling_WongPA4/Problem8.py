# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description: Write a program to calculate the exponent of given number. Please enter an integer indicating the base: 3
#Please enter a positive integer indicating the exponent: 4
#1 3 9 27 81

def main():
    expo()

def expo():
    m = int(input("Please enter an integer indicating the base: "))
    n = int(input("Please enter a positive integer indicating the exponent: "))
    for i in range(n + 1):
        print(m ** i, end=" ")  #computing step, and output for each time

main()