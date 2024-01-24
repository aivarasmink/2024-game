import logic
import gui_2048
import PySimpleGUI as sg

# logic.py

import random

def start_game():
    mat = [[0] * 4 for _ in range(4)]
    add_new_2(mat)
    add_new_2(mat)
    return mat

def move(mat, direction):
    mat = transpose(mat) if direction in ['UP', 'DOWN'] else mat
    reverse = direction in ['DOWN', 'RIGHT']
    mat = [move_line(line, reverse) for line in mat]
    mat = transpose(mat) if direction in ['UP', 'DOWN'] else mat
    return mat

def move_line(line, reverse=False):
    line = sorted(line, reverse=reverse)
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            line[i], line[i + 1] = 0, 2 * line[i]
    line = [value for value in line if value != 0]
    line = [0] * (len(line) - len(line)) + line
    return line if not reverse else list(reversed(line))

def transpose(mat):
    return [list(row) for row in zip(*mat)]

def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        mat[i][j] = 2

def get_current_state(mat):
    if any(2048 in row for row in mat):
        return 'WON'
    if any(0 in row for row in mat):
        return 'GAME NOT OVER'
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] or mat[j][i] == mat[j + 1][i]:
                return 'GAME NOT OVER'
    return 'LOST'
