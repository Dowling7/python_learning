#Daoning Wang
#COSI 10A, Fall 2021
#Programming Assignment #2
#Problem 2
#Get change after typing in the price

def main():
    Problem2()

def Problem2():
    price=int(input("Enter price of item"))
    change=100-price#Firstly we fighure out change
    Qua=change//25
    Dim=change%25//10
    Nic=change%25%10//5
    print("You bought an item for" ,price,"cents and gave me a dollar, so your change is")
    print(Qua, "quarters,\n")
    print(Dim, "dimes,\n")
    print(Nic, "nickel")

main()