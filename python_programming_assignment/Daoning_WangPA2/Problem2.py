#Daoning Wang
#COSI 10A, Fall 2021
#Programming Assignment #2
#Problem2
#Convert miles to kilometers

def main():
    Problem2()

def Problem2():
    mile = float(input("Enter a length in miles:"))
    km = mile * 1.60934  # Convert mile into km
    print(mile, "miles is %.2f" % km, "kilometers")#We only need two decimal points
main()