import random

print("H A N G M A N")

games = ['python', 'java', 'kotlin', 'javascript']
selected_letter = set()
attempt_letter = set()
answer = random.choice(games)
answer_set = set(answer)
number_of_tries = 8



def guess_next_letter():
    global number_of_tries
    print_answer()
    letter = input('Input a letter:')

    if len(letter) > 1:
        print('You should input a single letter')
    elif not letter.islower() :
        print('Please enter a lowercase English letter')
    elif letter in attempt_letter:
        print("You've already guessed this letter")
    elif letter not in answer:
        number_of_tries -= 1
        print("That letter doesn't appear in the word")
    else:
        selected_letter.add(letter)

    attempt_letter.add(letter)

    if number_of_tries == 0:
        print("You lost!")
        return

    if answer_set == selected_letter:
        print_answer()
        print("You guessed the word!")
        print("You survived!")
        return

    guess_next_letter()


def print_answer():
    selected_answer = ''.join([x if x in selected_letter else '-' for x in answer])
    print("")
    print(selected_answer)


play = True
while play:
    selection = input('Type "play" to play the game, "exit" to quit: ')
    if selection == 'play':
        guess_next_letter()
    elif selection == 'exit':
        play = False
