# Daoning Wang
# COSI 10a, Fall 2021
# Programming Assignment #3
#
# Description: Write a program that produces diagram in PA3
def main():
    Prob3()

def Prob3():
    p = 5 #It has 6 lines, but the number of * is 5 in the first line, set it as a reference for each line
    for i in range(p + 1):
        print("*" * p, " " * i, "//" * p + "\\\\" * i, " " * i, "*" * p) #Each line is the combination of 6 parts
        p = p - 1  #Yeah, go to next line, number of * decrease by 1

main()