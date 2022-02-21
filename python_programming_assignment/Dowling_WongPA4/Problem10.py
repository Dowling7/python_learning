# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description: Calculating the interest of deposit
def main():
    cal()

def cal():
    n = int(input("For how many years do you want to save:"))
    print("Year\t Curr Balence\t Interest\t New Deposit\t New Balence")
    c = 1000.00
    for i in range(n):
        b = int(0.0065 * c * 100) / 100
        print(i, "\t\t", c, "\t\t", b, "\t", "\t100.0", "\t\t\t", end="")    #The balence shows up two times a line, one is initial
        c = c + b + 100.0
        c = int(c * 100) / 100
        print(c) #and one is balence after adding interest and new deposit

main()