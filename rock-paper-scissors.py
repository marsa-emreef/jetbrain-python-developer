import random
import os.path

EXIT = '!exit'
RATING = '!rating'
game_options = ["rock","paper","scissors"]


LOSE = -1
DRAW = 0
WIN = 1

def a_win_against_b(a,b):
    index_a = game_options.index(a)
    index_b = game_options.index(b)
    max_len = len(game_options)
    half = int((max_len - 1) / 2)
    lose_start_index = index_a - half
    if lose_start_index < 0:
        lose_side = game_options[:index_a] + game_options[max_len+lose_start_index:]
    else:
        lose_side = game_options[lose_start_index:index_a]
    if index_a == index_b:
        return DRAW
    elif lose_side.count(b) > 0:
        return WIN
    else:
        return LOSE



def validate_input(selection):
    return [EXIT,RATING].count(selection) > 0 or game_options.count(selection) > 0

def load_data():
    if os.path.isfile('rating.txt'):
        with open('rating.txt','r',encoding='utf-8') as rating:
            return rating.readlines()
    return []

def get_rating(data,user_name):
    for line in data:
        name, rating = line.strip().split()
        if name == user_name:
            return int(rating)
    return 0

def save_rating(rating,user_name,data):
    db_index = -1
    for i,line in enumerate(data):
        name,_ = line.strip().split()
        if name == user_name:
            db_index = i
    if db_index >=0:
        data[db_index] = f'{user_name} {rating}\n'
    else:
        data.append(f'{user_name} {rating}\n')

    with open('rating.txt','w',encoding='utf-8') as db:
        db.writelines(data)

def play_game():
    global game_options
    keep_playing = True
    user_name = input('Enter your name:').capitalize()
    print(f"Hello, {user_name}")
    options = input('').strip()
    if len(options) > 0:
        game_options = options.split(',')
    print("Okay, let's start")
    data = load_data()
    rating = get_rating(data,user_name)
    while keep_playing:
        user_selection = input()
        if not validate_input(user_selection):
            print('Invalid input')
            continue

        if user_selection == EXIT:
            keep_playing = False
            continue

        if user_selection == RATING:
            print(f'Your rating: {rating}')
            continue

        computer_selection = random.choice(game_options)
        result = a_win_against_b(user_selection,computer_selection)

        if result == WIN:
            rating += 100
            save_rating(rating,user_name,data)
            print(f'Well done. The computer chose {computer_selection} and failed')
        elif result == DRAW:
            rating += 50
            save_rating(rating,user_name,data)
            print(f'There is a draw ({computer_selection})')
        elif result == LOSE:
            print(f'Sorry, but the computer chose {computer_selection}')

    print('Bye!')

play_game()
