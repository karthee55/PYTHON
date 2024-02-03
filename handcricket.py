import random
print("TOSS to 'PLAY'\n")
choose=["ODD","EVEN"]
toss=["0","1","2","3","4","5","6"]

#Getting toss from player
while True:
    playertoss=input("Player-->Choose ODD or EVEN: ").upper()
    if playertoss== "ODD" or playertoss=="EVEN":
        print("\nplayer choosen:",playertoss)
        break
    else:
        print("!!!INVALID TOSS!!!   choose odd or even\n" )

#Getting toss from computer
if playertoss=="EVEN":
    computertoss="ODD"
else:
    computertoss="EVEN"    
print("computer choosen:",computertoss)

#Getting toss number from player
while True:
    try:
        playernum=int(input("\nPlayer-->Choose a number between 0 to 6 for Toss: "))
        if playernum >=0 and playernum<7:
            break
        else:
            print("!!invalid number!! \n") 
            print("\nplayer number is: ",playernum)
    except ValueError:
        print("Play Properly.")        

#Getting toss number from Computer
computernum= int(random.choice(toss))
print("computer number is: ",computernum)

#Toss calculation
toss_sum= playernum + computernum
if toss_sum % 2==0:
    print(f"\nThe sum of Toss is {toss_sum}, so it is 'EVEN'")
    toss_call="EVEN"
else:
    print(f"\nThe sum of Toss is {toss_sum}, so it is 'ODD'")
    toss_call="ODD"

#function for player batting first
def batting():
    print("\n///Player is Batting!!!")
    print("...Computer is Bowling!!!\n")
    bat1_score=0
    num1_balls=0
    while True:
        while True:
            try:
                player_bats=int(input("\nPlayer-->choose a shot between 0 to 6: "))
                if player_bats>=0 and player_bats<7:
                    break
                else:
                    print("!!INVALID SHOT!!")
            except ValueError:
                print("Play Properly.")

        computer_bowls=int(random.choice(toss))
        print("\ncomputer bowls :",computer_bowls)
        num1_balls+=1
        if player_bats==computer_bowls:
            print("\n!!!OUT!!!\n")
            print("player score : ",bat1_score)
            print("Number of balls faced:",num1_balls)
            break
        else:
            bat1_score+=player_bats
            print("Player current score is: ",bat1_score)

    #computer chasing
    print("\n...Player is Bowling!!!")
    print("///Computer is Batting!!!\n")
    print(f"Computer needs {bat1_score+1} to WIN!!")
    bat2_score=0
    num2_balls=0
    chasing_score=bat1_score+1
    while True:
        while True:
            try:
                player_bowls=int(input("\nPlayer-->choice to Bowl between 0 to 6: "))
                if player_bowls>=0 and player_bowls<7:
                    break
                else:
                    print("!!INVALID BALL!!")
            except ValueError:
                print("Play Properly.")

        computer_bats=int(random.choice(toss))
        print("\ncomputer bats :",computer_bats)
        num2_balls+=1
        if computer_bats==player_bowls:
            print("\n!!!OUT!!!\n")
            print("Computer score : ",bat2_score)
            print("Number of balls faced:",num2_balls)
            break
        else:
            bat2_score+=computer_bats
            print("Computer current score is: ",bat2_score)
            chasing_score=chasing_score-computer_bats
            print(f"Need {chasing_score} to Win")
            if bat2_score>bat1_score:
                break
    
    if bat1_score>bat2_score:
        difference=bat1_score-bat2_score
        print(f"\n!!!Player won by {difference} Runs!!!\n")
    elif bat1_score==bat2_score:
        print("\n The Game has been Tied\n")
    else:
        print("\n!!Computer Wins!!    by chasing the target\n")

#function for computer batting first
def bowling():
    print("\n...Player is Bowling!!!")
    print("///Computer is Batting!!!\n")
    bat1_score=0
    num1_balls=0
    while True:
        while True:
            try:
                player_bowls=int(input("\nPlayer-->choice to Bowl between 0 to 6: "))
                if player_bowls>=0 and player_bowls<7:
                    break
                else:
                    print("!!INVALID BALL!!")
            except ValueError:
                print("Play Properly.")

        computer_bats=int(random.choice(toss))
        print("computer bats :",computer_bats)
        num1_balls+=1
        if computer_bats==player_bowls:
            print("\n!!!OUT!!!\n")
            print("Computer score : ",bat1_score)
            print("Number of balls faced:",num1_balls)
            break
        else:
            bat1_score+=computer_bats
            print("Computer current score is: ",bat1_score)

    #Player is chasing
    print("\n///Player is Batting!!!")
    print("...Computer is Bowling!!!\n")
    print(f"Player needs {bat1_score+1} to WIN!!")
    bat2_score=0
    num2_balls=0
    chasing_score=bat1_score+1
    while True:
        while True:
            try:
                player_bats=int(input("\nPlayer-->choose a shot between 0 to 6: "))
                if player_bats>=0 and player_bats<7:
                    break
                else:
                    print("!!INVALID SHOT!!")
            except ValueError:
                print("Play Properly.")
        
        computer_bowls=int(random.choice(toss))
        print("\ncomputer bowls :",computer_bowls)
        num2_balls+=1
        if player_bats==computer_bowls:
            print("\n!!!OUT!!!\n")
            print("player score : ",bat2_score)
            print("Number of balls faced:",num2_balls)
            break
        else:
            bat2_score+=player_bats
            print("Player current score is: ",bat2_score)
            chasing_score=chasing_score-player_bats
            print(f"Need {chasing_score} to Win")
            if bat2_score>bat1_score:
                break

    if bat1_score>bat2_score:
        difference=bat1_score-bat2_score
        print(f"\n!!!Computer won by {difference} Runs!!!\n")
    elif bat1_score==bat2_score:
        print("\n The Game has been Tied\n")
    else:
        print("\n!!Player Wins!!    by chasing the target\n")

# asking bats or bowl
batorball=["BATTING","BOWLING"]        
if toss_call==playertoss:
    print("\nYou WON the Toss")
    while True:
        player_decides=input("\nChoose BATTING or BOWLING :").upper()
        if player_decides=="BATTING" or player_decides=="BOWLING":
            print("Player Choosen: ",player_decides)
            break
        else:
            print("!!INVALID!!\n")

    #player deciding
    if player_decides=="BATTING":
        batting()
    else:
        bowling()
else:
    print("\nComputer Won the Toss")
    computer_decides=random.choice(batorball)
    print("computer Choosen: ",computer_decides)
    if computer_decides=="BATTING":
        bowling()
    else:
        batting()                




    


           
    
