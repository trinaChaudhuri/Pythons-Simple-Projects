import random
guessesTaken = 0
number = random.randint(1, 20)
while guessesTaken < 6:
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Perfect guess")
if guess != number:
    number = str(number)
    print("Not a correct guess")