# write your code here
def reduce(lamda_function, list_array, initial_value):
    accumulator = initial_value
    for data in list_array:
        accumulator = lamda_function(accumulator, data)
    return accumulator


def vector_two_matrix(size):
    def reducer(accumulator, data):
        if len(accumulator) == 0:
            accumulator.append([])
        last_item_in_accumulator = accumulator[len(accumulator) - 1]
        if len(last_item_in_accumulator) == size:
            last_item_in_accumulator = []
            accumulator.append(last_item_in_accumulator)
        last_item_in_accumulator.append(data)
        return accumulator

    return reducer


def construct_possible_combination(matrix):
    # pull rows, cols, diag
    rows = [row for row in matrix]
    cols = [[] for index in rows[0]]  # here we are inserting empty cols
    # this is to setup the cols row
    for row in rows:
        for col_index, value in enumerate(row):
            cols[col_index].append(value)

    # this is to setup the left diagonal
    left_diag = []
    for row_index, row in enumerate(rows):
        left_diag.append(matrix[row_index][row_index])

    # this is to setup the right diagonal
    right_diag = []
    for row_index, row in enumerate(rows):
        right_diag.append(matrix[row_index][-1 * (row_index + 1)])

    all_possible_combination = rows + cols
    all_possible_combination.append(left_diag)
    all_possible_combination.append(right_diag)
    return all_possible_combination


def is_wins(all_possible_combination, xo):
    def all_combination_match(combination):
        for val in combination:
            if xo != val:
                return False
        return True

    for cmb in all_possible_combination:
        if all_combination_match(cmb):
            return True

    return False


def print_matrix(matrix):
    print('---------')
    for vector in matrix:
        text = ' '.join(vector).replace('_', ' ')
        print(f'| {text} |')
    print('---------')


def play_game(matrix):
    all_combination = construct_possible_combination(matrix)

    x_win = is_wins(all_combination, 'X')
    o_win = is_wins(all_combination, 'O')
    matrix_content = ''.join([''.join(x) for x in matrix])
    game_complete = ' ' not in matrix_content and '_' not in matrix_content

    xo_not_balance = abs(matrix_content.count('X') - matrix_content.count('O')) > 1

    if xo_not_balance:
        return 'Impossible'
    elif x_win and not o_win:
        return 'X wins'
    elif o_win and not x_win:
        return 'O wins'
    elif o_win and x_win:
        return 'Impossible'
    elif not o_win and not x_win and game_complete:
        return 'Draw'
    elif not o_win and not x_win and not game_complete:
        return 'Game not finished'


def enter_movement(matrix, move):
    coordinate = input('Enter the coordinates:').split()
    if len(coordinate) < 2:
        print('Please enter coordinate separate with space')
        enter_movement(matrix, move)
        return

    if not coordinate[0].isnumeric() or not coordinate[1].isnumeric():
        print('You should enter numbers!')
        enter_movement(matrix, move)
        return

    y, x = int(coordinate[0]), int(coordinate[1])

    if not (0 < x < 4 and 0 < y < 4):
        print('Coordinates should be from 1 to 3!')
        enter_movement(matrix, move)
        return
    y, x = (y - 1), (-1 * x)

    position_value = matrix[x][y]
    if position_value == 'X' or position_value == 'O':
        print('This cell is occupied! Choose another one!')
        enter_movement(matrix, move)
    else:
        matrix[x][y] = move


cells = '_________'
reducer = vector_two_matrix(3)
matrix = reduce(vector_two_matrix(3), list(cells), [])
play_game(matrix)
next_move = 'X'
game_result = 'Game not finished'

while game_result == 'Game not finished':
    print_matrix(matrix)
    enter_movement(matrix, next_move)
    game_result = play_game(matrix)
    next_move = 'O' if next_move == 'X' else 'X'

print_matrix(matrix)
print(game_result)
