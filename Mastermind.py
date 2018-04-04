# Based on board game Mastermind https://en.wikipedia.org/wiki/Mastermind_(board_game)
# Author Nathan
import random as rand


def gen_computer(arg):
    temp = []
    for num in range(arg):
        temp.append(rand.randint(0, 9))
    print("A random '" + str(arg) + "' digit number was generated for you to guess")
    # print("[Debug]" + str(temp))  # Uncomment for debug
    return temp


def check_guess(args):
    global won
    global correct
    correct = [0, 0]
    if args.isdigit and len(args) == len(computer):
        for i in range(len(args)):
            if str(args[i]) == str(computer[i]):
                correct[0] += 1
            elif str(computer).__contains__(str(args[i])):
                correct[1] += 1
            if correct[0] == len(args):
                won = True
        print(str(correct[0]) + " numbers are right and " + str(correct[1]) + " are right but in the wrong spot")
    else:
        print("Invalid input, try again")
        turn_count(-1)


def turn_count(arg):
    global turn
    turn += arg


def won_message(arg):
    print("The correct number was:")
    print(computer)
    if arg > 1:
        print("You won in " + str(arg) + " turns!")
    else:
        print("You won in " + str(arg) + " turn!")


turn = 0
won = False

difficulty = input("Select a difficulty with a number (do not recommend a numbers greater then 10)")
if difficulty.isdigit():
    computer = gen_computer(int(difficulty))
else:
    print("Invalid difficulty input defaulting to '4'")
    computer = gen_computer(4)

while won is False:
    turn_count(1)
    print("Turn number " + str(turn))
    check_guess(input("Take your guess:"))
won_message(turn)
