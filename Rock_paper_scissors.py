# rock paper scissor

import random
import re


game = 0
win = 0
choices = ["R", "P", "S"]

while True:
    pick = random.choice(choices)
    print("\nRock Paper Scissors Shoot!")
    player = raw_input("Pick your weapon: [R]ock, [P]aper or [S]cissors\n")
    if re.match("[nN]",player):
        break
    if not re.match("[rRpPsS]",player):
        print("Pick [R]ock, [P]aper or [S]cissors!")
        print("[N] to end game.")
        continue
    print("You choose {}!".format(player.upper()))
    if player.upper() == pick:
        print("Tie!")
    elif (player.upper() == "R" and pick == "S") or (player.upper() == "S" and pick == "P") or (player.upper() == "P" and pick == "R"):
        print("You Win!")
        game += 1
        win += 1
    else:
        print("You lose.")
        game += 1
    
try:
    rate = win/game
except ZeroDivisionError:
    rate = 0
finally:
    print("Win rate: {}".format(rate))
