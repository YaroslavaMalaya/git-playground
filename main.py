import words_fetcher
import random


def congratulate_user():
    print(f"Congratulations, you won! your words: {guesses}")
    print("=============================")
    print("= Congratulations! You won! =")
    print("=============================")


def say_if_loser():
    print("=============================")
    print("= Unfortunately, you lost. =")
    print("=============================")


def is_game_over(errors):
    return guessed == WORDS_TO_WIN or errors == ERRORS_TO_LOSE


def guess_is_valid(candidate, errors):
    for letter in candidate:
        if letter not in word:
            print(f"You can not use letter {letter}")
            errors += 1
            return False, errors
        count = word.count(letter)
        if count < candidate.count(letter):
            print(f"You can use letter {letter} only {count} times")
            errors += 1
            return False, errors
    return True


guessed = 0
errors = 0

guesses = []

WORDS_TO_WIN = 5
ERRORS_TO_LOSE = 3

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
full_list = words_fetcher.fetch_words(min_letters=3, max_letters=9)
word = words[random.randrange(0, len(words))]

print(f"Can you make up {WORDS_TO_WIN} words from letters in word provided by me?")
print(f"Your word is '{word}'")


while not is_game_over(errors):
    guess = input("Your next take: ")

    if not guess_is_valid(guess, errors):
        continue

    if guess in full_list:
        if guess in guesses:
            errors += 1
            print(f"You can't use this word again. {WORDS_TO_WIN- guessed} to go")
        else:
            guessed += 1
            guesses.append(guess)
            if guessed == WORDS_TO_WIN:
                congratulate_user()
                exit()
            elif WORDS_TO_WIN == 0:
                say_if_loser()
                exit()
            print(f"That's right! {WORDS_TO_WIN - guessed} to go")
    else:
        errors += 1
        print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
