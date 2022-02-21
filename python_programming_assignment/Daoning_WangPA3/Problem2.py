# Daoning Wang
# COSI 10a, Fall 2021
# Programming Assignment #3
#
# Description: The factorial function is used frequently in probability problems. The factorial of a
# positive integer n (written n! and pronounced “n factorial”) is equal to the product of the
# positive integers from 1 to n
def main():
    Prob2()

def Prob2():
    for j in range(3): #It need three input, so give a loop in range(3)
        number = int(input("Enter a number: "))
        fact = 1 #give a value first, then use loop to calculate the value of factorial
        for i in range(1, number + 1): #The process of calculating the factorial
            fact = fact * i
        print(number, end="")
        print("! =", fact)

main()