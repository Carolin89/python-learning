import random, sys


def get_move_string(move):
    if move == 'r':
        return "ROCK"
    elif move == 'p':
        return "PAPER"
    elif move == 's':
        return "SCISSORS"

print("ROCK, PAPER, SCISSORS")
losses = 0
wins = 0
ties = 0

while True:
    print(str(wins) + "Wins, " + str(losses) + " Losses, "+ str(ties) +" Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    userMove = input();
    computerMove = random.randint(1,3)


    if computerMove == 1:
        computerMoveString = "p"
    elif computerMove == 2:
        computerMoveString = "r"
    else: computerMoveString = "s"

    userMoveStringFull = get_move_string(userMove)
    computerMoveStringFull = get_move_string(computerMoveString)

    if userMove == "q":
        sys.exit()

    if userMove not in ['r', 'p', 's']:
        print("Invalid input. Please enter 'r', 'p', 's', or 'q'.")
        continue

    print(userMoveStringFull + " versus...")
    print(computerMoveStringFull)
    
    if userMove == computerMoveString:
        print("It is a tie!")
        ties += 1
        continue
    if (userMove == "s" and computerMoveString == "r") or (userMove == "r" and computerMoveString == "p") or (userMove == "p" and computerMoveString=="s"):

        print("You lose!")
        losses+=1
    else:
        print("You win!")
        wins+=1