import random

cpu_wins = 0
player_wins = 0

while True :
    choices = ["R", "P", "S"]
    CPU = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Enter R-Rock, P-Paper, S-Scissors :")

    if player == CPU:
        print("CPU: ", CPU)
        print("Player: ", player)
        print("Tie")

    elif player == "R":
        if CPU == "P":
            cpu_wins += 1
            print("CPU: ", CPU)
            print("Player: ", player)
            print("You Lose")
        if CPU == "S":
            player_wins += 1
            print("CPU: ", CPU)
            print("Player: ", player)
            print("You Win")

    elif player == "P":
        if CPU == "S":
            cpu_wins += 1
            print("CPU: ", CPU)
            print("Player: ", player)
            print("You Lose")
        if CPU == "R":
            player_wins += 1
            print("CPU: ", CPU)
            print("Player: ", player)
            print("You Win")

    elif player == "S":
        if CPU == "P":
            player_wins += 1
            print("CPU: ", CPU)
            print("Player: ", player)
            print("You Win")
        if CPU == "R":
            cpu_wins += 1
            print("CPU: ", CPU)
            print("Player: ", player)
            print("You Lose")

    print("You won ", player_wins, " times")
    print("CPU won ", cpu_wins, " times")
    play_again = input("Play again? Y/N: ")

    if play_again != "Y":
        break