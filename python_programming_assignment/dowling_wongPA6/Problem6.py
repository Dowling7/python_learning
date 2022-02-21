# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #6
#
# Description: Write a program that allows the user to play many rounds of the Rock Paper Scissor game (the
#user will decide when to end the game). The user and computer will each choose between three
#items: rock (defeats scissor, but loses to paper), paper (defeats rock, but loses to scissors), and
#scissors (defeats paper, but loses to rock). If the player and computer choose the same item, the
#game is a tie. Extend this program to include different algorithmic strategies for choosing the best
#item. Should the computer always pick a particular item or a repeating pattern of items? Should it
#count the number of times the opponent chooses various items and base its strategy on this
#history? Be creative here. Each strategy should be in its own method, and at the start of a round of
#games the user should be able to choose which strategy to play against. Include at least two
#strategies.

import random
def main():
    RPS()
    
def RPS():
    print("please choose your strategy")
    choice=int(input("1 for random choice, 2 for using the same item all the time"))
    print("When you entered the game, you could type Rock, Paper, Scissors, type exit to exit the game")
    #Firstly, choose the strategy
    if choice == 1:
        randomchoice()
    elif choice ==2:
        onethrough()
        
def onethrough():
    computer="Rock"
    #set player to False
    player = False
    while player == False:
#set player to True by the process
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        elif player != "exit":
            print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
        if player =="exit":
            player= True
            print("You now exit the game")
        else:
            player = False
    
     

    
def randomchoice():
#assign a random play to the computer
    t=random.randint(0,2)
    if t==0:
        computer="Rock"
    elif t==1:
        computer="Paper"
    else:
        computer="Scissors"

#set player to False
    player = False

    while player == False:
#set player to True
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        elif player != "exit":
            print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
        if player =="exit":
            player= True
            print("You now exit the game")
        else:
            player = False
    
        t=random.randint(0,2)
        if t==0:
            computer="Rock"
        elif t==1:
            computer="Paper"
        else:
            computer="Scissors"

main()