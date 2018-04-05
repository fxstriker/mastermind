# Based on board game Mastermind https://en.wikipedia.org/wiki/Mastermind_(board_game)
# Author Nathan
import random


def gen_computer(difficulty_input):
    temp = []
    for num in range(difficulty_input):
        temp.append(random.randint(0, 9))
    print("A random '%s' digit number was generated for you to guess" % difficulty_input)
    # print("[Debug]" + str(temp))  # Uncomment for debug
    return temp


def check_guess(args):
    global turn
    global won
    global correct
    correct = [0, 0]
    if args.isdigit() and len(args) == len(computer):
        for i in range(len(args)):
            if str(args[i]) == str(computer[i]):
                correct[0] += 1
            elif str(computer).__contains__(str(args[i])):
                correct[1] += 1
            if correct[0] == len(args):
                won = True
        print("%d numbers are right and %d are right but in the wrong spot" % (correct[0], correct[1]))
    else:
        print("Invalid input, try again")
        turn -= 1


def won_message(turn_num):
    print("The correct number was:")
    print(computer)
    temp = "turn!"
    if turn_num > 1:
        temp = "turns!"
    print("You won in %s %s" % (turn_num, temp))


turn = 0
won = False

difficulty = input("Select a difficulty with a number (do not recommend a numbers greater then 10)")
if difficulty.isdigit():
    computer = gen_computer(int(difficulty))
else:
    print("Invalid difficulty input defaulting to '4'")
    computer = gen_computer(4)
while won is False:
    turn += 1
    print("Turn number %s" % turn)
    check_guess(input("Take your guess:"))
won_message(turn)
