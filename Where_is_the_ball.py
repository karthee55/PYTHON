from random import shuffle

# function for shuffling the ball

def shuffle_ball(ball):
    shuffle(ball)
    return ball


# function for player guessing
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("pick a number: 0, 1 or 2 ")
    return int(guess)    
   

# function for finding the ball with the user guess
def finding_ball(ball,guess):
    if ball[guess]=='O':
        print("correct!\n")
    else:
        print("Wrong Guess!\n")
    
 



# function for playing the game
def game():
    ball=['','O','']
    shuffuled_ball=shuffle_ball(ball)
    print("!!! WHERE IS THE BALL !!!\n")
    print("__ O __\n")

    guess=player_guess()
    finding_ball(shuffuled_ball,guess)

    print(shuffuled_ball)

# calling the functions
game()
while True:
    play_again=input("\nWould you like to play again (yes/no):").upper()
    if play_again == "YES":
        game()
    elif play_again== "NO":
        print("\n!!! GAME OVER !!!")
        break
    else:
        print('''\n      !!INVALID!!
              Say YES or NO\n''')

    

