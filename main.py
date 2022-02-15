import random
import math


def choose_range():
    print("Choose a range of numbers!")
    lowest = int(input("Lowest: "))
    highest = int(input("Highest: "))
    while highest <= lowest:
        print(f"\nChoose a number greater than {lowest}!")
        highest = int(input("Highest: "))
    return lowest, highest


def pick_number(beginning, end):
    correct_number = random.randrange(beginning, end)
    print(f"\nI chose a number between {beginning} and {end}. Try to guess it!")
    return correct_number


def max_nr_of_guesses(beginning, end):
    max_guesses = math.ceil(math.log(end - beginning + 1, 2))
    print(f"You have a maximum of {max_guesses} attempts.")
    return max_guesses


def guess(correct_number):
    global count
    number = int(input("\nYour guess:"))
    if number > correct_number:
        print("Your guess is too high. Try again!")
        count += 1
    elif number < correct_number:
        print("Your guess is too low. Try again!")
        count += 1
    elif number == correct_number:
        print("Correct! You won!")
        global win
        win = True


win = False
lost = False
count = 0

a, b = choose_range()
correct_nr = pick_number(a, b)
maximum = max_nr_of_guesses(a, b)

while not win and not lost:
    guess(correct_nr)
    if count >= maximum:
        print(f"\nMaximum number of attempts reached.\nCorrect number: {correct_nr}\nGame over!")
        lost = True

#nyaa
