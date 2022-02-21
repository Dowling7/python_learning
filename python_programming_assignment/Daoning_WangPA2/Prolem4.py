#Daoning Wang
#COSI 10A, Fall 2021
#Programming Assignment #2
#Proble4
#Guild for cookies

def main():
    Problem4()

def Problem4():
    amount=float(input("Please enter the amount of cookies you want to make:"))
    #If a person want to do some float number of cookies, we cannot deprive their right
    sugar=1.5/48*amount
    butter=1.0/48*amount
    flour=2.75/48*amount
    print("You need")
    print("%.2f"%sugar,"cups of sugar")#Keep only two decimals.
    print("%.2f"%butter," cups of butter")
    print("%.2f"%flour, "cups of flour")

main()
