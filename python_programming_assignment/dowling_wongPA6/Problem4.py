# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #6
#
# Description: Write a program that accepts two string variables, first and last, which the user should populate
#with his or her name. First, convert both strings to all lowercase. Your program should then create
#a new string that contains the full name in pig latin with the first letter capitalized for the first and
#last name. Use only the pig latin rule of moving the first letter to the end of the word and adding
#“ay”. Output the pig latin name to the screen.
def main():
    FnL()

def FnL():
    first=input("Please input your first name: ")
    last=input("Please input your last name: ")
    first=first.lower()
    last=last.lower()
    #First we lower all the letters
    convert(first)
    #convert two part separately
    print(" ",end="")
    convert(last)
    
def convert(x):
    b=x[0]
    c=x[1:]
    a=c[0]
    d=c[1:]+b+"ay"
    print(c[0].upper(), end="")
    #Print the final result in two parts
    print(d,end="")
    
main()