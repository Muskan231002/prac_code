import random
i=int(input("Enter how many rounds you want to play : \n"))
choices=["stone","paper","scissor"]
computer_score=0
player_score=0
for j in range(i):
    player=input("choose stone,paper,scissor : \n")
    computer=random.choice(choices)
    print(f"the computer chose {computer}")
    if computer=="stone":
        if player== "stone":
            print("its a draw")
        elif (player=="paper"):
            player_score+=1
            print("player won")
        else:
            computer_score+=1
            print("computer won")  
            
    elif computer=="paper":
        if player== "paper":
            print("its a draw")
        elif (player=="stone"):
            computer_score+=1
            print("computer won")
        else:
            player_score+=1
            print("player won")  
        
    else:
        if player== "scissor":
            print("its a draw")
        elif (player=="stone"):
            player_score+=1
            print("player won")
        else:
            computer_score+=1
            print("computer won") 
    print("------------------------------------------------------------------")
    print(f"computer score = {computer_score} | player score = {player_score}")
    print("------------------------------------------------------------------")
        
    