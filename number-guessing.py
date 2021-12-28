# number guessing

import random

leaderboard = []


def show_score():
    if len(leaderboard) != 0:
        min = 999
        for indx, score in enumerate(leaderboard):
            if score[0] < min:
                min = score[0]
                player = score[1]
        print("Best score is {} by {}".format(min,player))
    else:
        print("There is no best score yet.")

def start_game():
    rdm_nbr = int(random.randint(1,10))
    player = input("Enter your name: ")
    play = input("{}, let's play a game? Y/N ".format(player))
    count = 0
    while play.upper() == "Y":
        guess = input("Pick a number between 1 and 10:")
        try:
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Number is not within range.")
            if int(guess) == rdm_nbr:
                count += 1
                print("You got it in {} rounds!".format(count))
                new_rec = tuple((count,player))
                leaderboard.append(new_rec)
                show_score()
                again = input("Play again? Y/N")
                if again.upper() == "Y":
                    count = 0
                    rdm_nbr = int(random.randint(1,10))
                else:
                    print("ok! bye!")
                    break
            elif int(guess) > rdm_nbr:
                count += 1
                print("It's lower than {}".format(int(guess)))
            elif int(guess) < rdm_nbr:
                count += 1
                print("It's higher than {}".format(int(guess)))
        except ValueError as err:
            print("That's not valid.")
            print("({})".format(err))
    else:
        print("ok! bye!")
if __name__ == "__main__":
    start_game()
                
