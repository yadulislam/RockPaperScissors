import random
print("Welcome to Rock Paper Scissors!")
print(".................................")
cpuscore = 0
playerscore = 0
tiescore = 0
possibleHands = ["Rock", "Paper", "Scissors"]
def checkforwinner(playerHand, computerhand):
    if playerHand == "Rock" and computerhand == "Paper":
        print("Sorry you lost :( ")
        return "cpu"
    elif playerHand == "Rock" and computerhand == "Scissors":
        print("Congrats! You have won :) ")
        return "player"
    elif playerHand == "Scissors" and computerhand == "Paper":
        print("Congrats! You have won :) ")
        return "player"
    elif playerHand == "Scissors" and computerhand == "Rock":
        print("sorry you lost :( ")
        return "cpu"
    elif playerHand == "Paper" and computerhand == "Rock":
        print("Congrats! You have won :) ")
        return "player"
    elif playerHand == "Paper" and computerhand == "Scissors":
        print("sorry you lost :( ")
        return "cpu"
    else:
        print("It is a tie, play again!")
        return "Tie"
#start game loop
while(playerscore != 3 and cpuscore !=3):
    while True:
        playerHand = input("\nPick a hand. Rock, Paper, or Scissors: ")
        if(playerHand == "Rock" or playerHand == "Paper" or playerHand == "Scissors"):
            break
        else:
            print("Invalid input, try again.")
    #generate computer pick
    computerHand = random.choice(possibleHands)
    #print results
    print("Your hand:", playerHand)
    print("cpu hand:", computerHand)
    result = checkforwinner(playerHand, computerHand)
    if result == "player":
        playerscore +=1
    elif result == "cpu":
        cpuscore +=1
    else:
        tiescore +=1
    print("Your score: ", playerscore, "cpu", cpuscore, "Ties", tiescore)
print("Game over! Thank you for playing :)")