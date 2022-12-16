import random 
 
play = ["Rock", "Paper", "Scissors"]


computer = play[random.randint(0,2)] 
 
player = play


while player == play: 
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
            print("You lose!", computer, "cuts", player) 
        else: 
            print("You win!", player, "covers", computer) 
    elif player == "Scissors": 
        if computer == "Rock": 
            print("You lose...", computer, "smashes", player) 
        else: 
            print("You win!", player, "cuts", computer) 
    else: 
        print("That's not a  play. Check the spelling!") 
   
    
    anotherchance = int(input ("play again :'1' for yes and '0' for no "))
    if anotherchance==0:
       print ("THANK YOU")
    else:
        player = play
        computer = play[random.randint(0,2)] 
        
         

    
