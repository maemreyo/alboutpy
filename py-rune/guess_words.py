import random

words = ['father', 'enterprise', 'science', 'programming',
         'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
word = random.choice(words)

guesses = ''

turns = 10

while turns > 0:
    print(f"You have {turns} turns left")

    guessed_all = True
    for c in word:
        if c in guesses:
            print(c, end=" ")
        else:
            print('_', end=' ')
            guessed_all = False
    print()

    if not guessed_all:
        guess = input("Guess a char: ")
        guesses = guesses + guess
        if guess not in word:
            turns = turns - 1
    else:
        turns = 0
