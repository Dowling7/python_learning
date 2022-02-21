# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #5
#
# Description:Write a program that prompts the user for a positive integer number (not bigger than 4999) and
# displays it in Roman numerals.

def main():
    inte = int(input("Please input an integer"))
    sum(inte)

def sum(x):
    if x>4999:
        print("error, please input a number less than 4999")#We don't take number bigger than 4999 into consideration
        return
    else:
        torom(x)#This is the function to get the Roman numeral

def toromstep(num, rom, val):#This is the step to figure out each part of roman numeral
    res = ''
    d = int(num // val)
    num = num % val
    res += rom * d
    print(res, end="")
    return d

def torom(n):

    M = toromstep(n, "M", 1000)
    n = n - (M * 1000)
    CM = toromstep(n, "CM", 900)
    n = n - (CM * 900)
    D = toromstep(n, "D", 500)
    n = n - (D * 500)
    CD = toromstep(n, "CD", 400)
    n = n - (CD * 400)
    C = toromstep(n, "C", 100)
    n = n - (C * 100)
    XC = toromstep(n, "XC", 90)
    n = n - (XC * 90)
    L = toromstep(n, "L", 50)
    n = n - (L * 50)
    XL = toromstep(n, "XL", 40)
    n = n - (XL * 40)
    X = toromstep(n, "X", 10)
    n = n - (X * 10)
    IX = toromstep(n, "IX", 9)
    n = n - (IX * 9)
    V = toromstep(n, "V", 5)
    n = n - (V * 5)
    IV = toromstep(n, "IV", 4)
    n = n - (IV * 4)
    I = toromstep(n, "I", 1)

main()

