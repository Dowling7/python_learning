# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #7
#
# Description:Your program allows the user to play a game in which the program thinks of a random integer
#and accepts guesses from the user until the user guesses the number correctly. After each
#incorrect guess, you will tell the user whether the correct answer is higher or lower. Your
#program must exactly reproduce the format and behavior of the logs in this document.

import random
import math
def main():
    guess()
    
def summary(a,b,c):
    print("Overall results:")
    print("Total games =", a)
    print("Total guesses =", b)
    print("Guesses/game =", round(b/a))
    print("Best game =", c)
    
    
    
def guess():
    print("""This game provide your opportunity to guess a number between 1 and 100
             If you wanna continue the game at the end, just type any word start with y or Y
             If you wanna quit at the end, type anything else than y.""")
    print()
    print("I'm thinking of a number between 1 and 100...")
    pc_num=random.randint(1,100)
    player=False    #set player as false at first, because user definitly want to play at first
    count=0         #I would say this variables are useful, so declare them at the very begining
    games=1
    tot=0
    best=99999
    while player==False:
        player=input("Your guess? ")
        if int(player) != pc_num:
            count+=1
            player=int(player)
            if int(player) > pc_num:
                print("It's lower.")
                player= False
            else:
                print("It's higher.")
                player= False
        else:
            count+=1
            print("You got it right in "+str(count)+" guesses!")
            choice=input("Do you want to play again? ")
            if count< best:
                best=count
            if choice[0]=="y" or choice[0]=="Y":
                player= False 
                print()
                print("I'm thinking of a number between 1 and 100...")
                pc_num=random.randint(1,100)
                games+=1
                tot+=count
                count=0
    
            else:
                tot+=count
                player= True
                summary(games, tot, best)
                
           
        
main()