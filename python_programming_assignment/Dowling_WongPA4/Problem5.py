# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description: Write a program that produces the following output. Use for loops and string
# multiplication to capture the structure of the figure.
#!!!!!!!!!!!!!!!!!!!!!!
#\\!!!!!!!!!!!!!!!!!!//
#\\\\!!!!!!!!!!!!!!////
#\\\\\\!!!!!!!!!!//////
#\\\\\\\\!!!!!!////////
#\\\\\\\\\\!!//////////

def main():
    draw(6)

def draw(n):
    for i in range(n):
        print("\\\\" * i + "!" * (22 - 4 * i) + "//" * i)   #Line by line, each line could be divided into 3 parts


main()

