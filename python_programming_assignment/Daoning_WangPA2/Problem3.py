#Daoning Wang
#COSI 10A, Fall 2021
#Programming Assignment #2
#Problem3
#calculate the average number

def main():
    Problem3()

def Problem3():
    print("Please type in three numbers, press enter to finish typing")#prompt
    x, y, z = float(input()), float(input()), float(input())#receiving three numbers
    average = (x + y + z) / 3#calculation
    print(average)

main()