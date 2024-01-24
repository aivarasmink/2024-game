import random

def start_game():
    mat = [[0] * 4 for _ in range(4)]
    add_new_2(mat)
    add_new_2(mat)
    return mat

def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        mat[r][c] = 2

def compress(mat):
    changed = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                mat[i][pos], mat[i][j] = mat[i][j], mat[i][pos]
                if j != pos:
                    changed = True
                pos += 1
    return changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3, 0, -1):
            if mat[i][j] == mat[i][j - 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j - 1] = 0
                changed = True
    return changed

def move_left(mat):
    changed = compress(mat)
    changed = merge(mat) or changed
    compress(mat)
    return changed

def move_right(mat):
    reverse(mat)
    changed = move_left(mat)
    reverse(mat)
    return changed

def move_up(mat):
    transpose(mat)
    changed = move_left(mat)
    transpose(mat)
    return changed

def move_down(mat):
    transpose(mat)
    changed = move_right(mat)
    transpose(mat)
    return changed

def reverse(mat):
    for i in range(4):
        mat[i] = mat[i][::-1]

def transpose(mat):
    for i in range(4):
        for j in range(i + 1, 4):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'NOT MOVE'
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'NOT MOVE'
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'NOT MOVE'
    return 'LOST'
