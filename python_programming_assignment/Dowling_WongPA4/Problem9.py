# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #4
#
# Description: Rotation symmetry. The first line should start with the
# minimum, each line that follows should start with the next-higher number. The sequence of
# numbers on a line wraps back to the minimum after it hits the maximum.

def main():
    rota()

def rota():
    m = int(input("Please enter a minimum integer: "))
    n = int(input("Please enter a maximum integer: "))
    for i in range(m, n + 1):
        for j in range(i, n + 1):  #just divide each line into two parts, so it can rotate
            print(j, end="")
        for j in range(m, i):
            print(j, end="")
        print()

main()
