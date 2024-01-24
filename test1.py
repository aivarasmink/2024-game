import logic
import gui_2048
import PySimpleGUI as sg

def main_window(user_theme, mat):
    sg.theme(user_theme)
    buttons = [[sg.Button('', size=(5, 2), pad=(5, 5), key=(i, j), font="Any 15") for j in range(4)] for i in range(4)]

    layout = [
        [buttons[0][0], buttons[0][1], buttons[0][2], buttons[0][3]],
        [buttons[1][0], buttons[1][1], buttons[1][2], buttons[1][3]],
        [buttons[2][0], buttons[2][1], buttons[2][2], buttons[2][3]],
        [buttons[3][0], buttons[3][1], buttons[3][2], buttons[3][3]],
        [sg.Button('\u21C7', font="Arial 22", pad=((40,5), (0,0)), key="-LEFT-"),
         sg.Button('\u21C8', font="Arial 22", key="-UP-"),
         sg.Button('\u21CA', font="Arial 22", key="-DOWN-"),
         sg.Button('\u21C9', font="Arial 22", key="-RIGHT-")],
        [sg.Button("New Game", size=11, pad=((40,10), (0,0))), sg.Button("Exit", size=11)],
        [sg.Button("Change Theme", size=20, pad=((55,10), (30,0)))],
        [sg.Button("The game creator's", size=20, pad=((55,10), (10,0)))]
    ]

    window = sg.Window("2048", layout)

    return window, buttons

if __name__ == '__main__':
    mat = logic.start_game()
    user_theme = "DarkAmber"
    window, buttons = main_window(user_theme, mat)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-UP-":
            mat, flag = logic.move_up(mat)
        elif event == "-DOWN-":
            mat, flag = logic.move_down(mat)
        elif event == "-LEFT-":
            mat, flag = logic.move_left(mat)
        elif event == "-RIGHT-":
            mat, flag = logic.move_right(mat)
        elif event == "New Game":
            mat = logic.start_game()
        elif event == "The game creator's":
            gui_2048.titles(user_theme)
        elif event == "Change Theme":
            user_theme = gui_2048.theme_select(user_theme)
            window.close()
            sg.theme(user_theme)
            window, buttons = main_window(user_theme, mat)

        for i in range(4):
            for j in range(4):
                buttons[i][j].update(mat[i][j] if mat[i][j] != 0 else '')

    window.close()
