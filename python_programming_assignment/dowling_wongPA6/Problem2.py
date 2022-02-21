# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #6
#
# Description: Write a program that prompts the user for a string and an integer and prints out the string with
#each character repeated the same number of times as the integer entered by the user. Your
#possible interaction with the user should be like:
#Please enter a String: red
#Please enter a multiplier for each character to repeat: 4
#I got: rrrreeeedddd

def main():
    init=input("Please enter a String: ")
    time=int(input("Please enter a multiplier for each character to repeat:"))
    splitmulti(init,time)
#Give initial string and repeat time to the program 
def splitmulti(a,b):
    print("I got: ", end="")
    for letter in a:
#I have asked this on LATTE discussion, one of our dear TAs said it could be used here
        print(letter*b,end="")
    
main()