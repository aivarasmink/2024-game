import PySimpleGUI as sg
from logic_test import start_game, move_up, move_down, move_left, move_right, add_new_2

def main_window(user_theme, mat):
    sg.theme(user_theme)
    buttons = [[sg.Button('', size=(5, 2), pad=(5, 5), key=(i, j), font="Any 15") for j in range(4)] for i in range(4)]

    layout = [
        [buttons[0][0], buttons[0][1], buttons[0][2], buttons[0][3]],
        [buttons[1][0], buttons[1][1], buttons[1][2], buttons[1][3]],
        [buttons[2][0], buttons[2][1], buttons[2][2], buttons[2][3]],
        [buttons[3][0], buttons[3][1], buttons[3][2], buttons[3][3]],
        [sg.Button('\u21C7', font="Arial 22", pad=((40, 5), (0, 0)), key="-LEFT-"),
         sg.Button('\u21C8', font="Arial 22", key="-UP-"),
         sg.Button('\u21CA', font="Arial 22", key="-DOWN-"),
         sg.Button('\u21C9', font="Arial 22", key="-RIGHT-")],
        [sg.Button("New Game", size=11, pad=((40, 10), (0, 0))), sg.Button("Exit", size=11)],
    ]

    window = sg.Window("2048", layout)

    return window, buttons

def update_buttons(window, buttons, mat):
    for i in range(4):
        for j in range(4):
            button_key = (i, j)
            window[button_key].update(mat[i][j] if mat[i][j] != 0 else '')

if __name__ == '__main__':
    mat = start_game()
    user_theme = "DarkAmber"
    window, buttons = main_window(user_theme, mat)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-UP-":
            if move_up(mat):
                add_new_2(mat)
        elif event == "-DOWN-":
            if move_down(mat):
                add_new_2(mat)
        elif event == "-LEFT-":
            if move_left(mat):
                add_new_2(mat)
        elif event == "-RIGHT-":
            if move_right(mat):
                add_new_2(mat)
        elif event == "New Game":
            mat = start_game()
        update_buttons(window, buttons, mat)

    window.close()
