import random

print("----------rock / paper / scissor----------")

lap = int(input("How many rounds do you want to play? "))


for i in range(1, lap+1):
    user = input("Choise? ")
    number = random.randint(1, 3)
    player = ""
    if number == 1:
        player = "rock"
        print("player choise rock")
    elif number == 2:
        player = "paper"
        print("player choise paper")
    elif number == 3:
        player = "scissor"
        print("player choise scissor")
    if player == "rock" and user == "paper":
        print("User win")
    elif player == "rock" and user == "scissor":
        print("Player win")
    elif player == "scissor" and user == "rock":
        print("Player win")
    elif player == "paper" and user == "scissor":
        print("User win")
    elif player == "scissor" and user == "paper":
        print("Player win")
    elif player == "scissor" and user == "rock":
        print("User win")
    else:
        print("Draw")
