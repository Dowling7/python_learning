# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description:The Fibonacci numbers are a sequence of integers in which the first two elements are
# 1 and each following element is the sum of the two preceding elements.

def main():
    fibo(12)


def fibo(n):
    a = 1    #The fist number of fibonacci sequence are 1
    b = 1
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, n):
        c = a + b    #make a substitution, let c be the result of a+b
        a = b        #and  then let a,b have new values, for the next loop
        b = c
        print(c, end=" ")

main()


