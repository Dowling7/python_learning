# Daoning Wang
# COSI 10a, Fall 2021
# Programming Assignment #3
#
# Description: This problem asks the user to enter an exponent. Then calculate and print 2 to the
# power of that exponent starting from 20 up to the user's number, inclusively
def main():
    Prob1()

def Prob1():
    number=int(input("Enter a number for exponent: ")) #This is to ask user give a number
    for i in range(number+1):
        print(2**i,"\t")  #In the loop, it calculate and print the exponent one at a time
        i=i+1

main()