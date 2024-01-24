import PySimpleGUI as sg
from random import randint

def new_game(n):
    matrix = [[0] * n for i in range(n)]
    return matrix

def game_state(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j + 1] == mat[i][j]:
                return 'not over'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    for k in range(len(mat) - 1):
        if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
            return 'not over'
    for j in range(len(mat) - 1):
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return 'not over'
    return 'lose'

def reverse(mat):
    new = []
    x = y = len(mat)
    for i in range(x):
        new.append([])
        for j in range(y):
            new[i].append(mat[i][y - j - 1])
    return new

def transpose(mat):
    new = []
    x = y = len(mat)
    for i in range(y):
        new.append([])
        for j in range(x):
            new[i].append(mat[j][i])
    return new

def cover_up(mat):
    x = y = len(mat)
    new = [x * [0] for i in range(y)]
    done = False
    for i in range(x):
        count = 0
        for j in range(y):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done

def merge(mat):
    done = False
    x = y = len(mat)
    for i in range(x):
        for j in range(y - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    return mat, done

def up(game):
    game = transpose(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(game)
    return game, done

def down(game):
    game = reverse(transpose(game))
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game, done

def left(game):
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    return game, done

def right(game):
    game = reverse(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = reverse(game)
    return game, done

SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
                         32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
                         512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
                   512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
FONT = ("Helvetica", 20, "bold")

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"

def main():
    layout = [[sg.Button('', key=(i, j), size=(5, 2), pad=(0, 0), button_color=('white', BACKGROUND_COLOR_DICT[0]))
               for j in range(GRID_LEN)] for i in range(GRID_LEN)]
    window = sg.Window('2048', layout, return_keyboard_events=True)

    game_matrix = new_game(GRID_LEN)
    generate_next(game_matrix)
    generate_next(game_matrix)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event in (KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT):
            direction = event[1]
            game_matrix, moved = move(direction, game_matrix)
            if moved:
                generate_next(game_matrix)
                update_gui(window, game_matrix)

    window.close()

def update_gui(window, matrix):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            elem = matrix[i][j]
            text = '' if elem == 0 else str(elem)
            window[(i, j)].update(text, button_color=('white', BACKGROUND_COLOR_DICT.get(elem, 'white')))

def generate_next(matrix):
    index = (randint(0, GRID_LEN - 1), randint(0, GRID_LEN - 1))
    while matrix[index[0]][index[1]] != 0:
        index = (randint(0, GRID_LEN - 1), randint(0, GRID_LEN - 1))
    matrix[index[0]][index[1]] = 2

def move(direction, matrix):
    if direction == 'w':
        return up(matrix)
    elif direction == 's':
        return down(matrix)
    elif direction == 'a':
        return left(matrix)
    elif direction == 'd':
        return right(matrix)
    else:
        return matrix, False

if __name__ == "__main__":
    main()
