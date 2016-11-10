import random

rounds = 1000
doors = ["sports car", "goat", "goat"]
win = 0
lose = 0
random_choice = doors[::]

for i in range(rounds):
    chance = random.randrange(0, 3)
    choice = doors[chance]

    def door_one(choice):
        if chance == 0:
            win += 1


    def door_two(choice):
        if chance == 1:
            win += 1


    def door_three(choice):
        if chance == 2:
            lose += 1


    def random_choice(choice):
        random_choice = (win * 0.5) * (lose * 0.5)


    def percentage(choice, rounds):
        percentage = (win/rounds) * 100


def main():
    print("Wins: " + str(win))
    print("Losses: " + str(lose))
    print("Random: " + str(random_choice))
    print("Percenage won: " + str(percentage)+"%")


if __name__ == "__main__":
    main()
