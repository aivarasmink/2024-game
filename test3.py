import logic
import gui_2048
import PySimpleGUI as sg

def create_game_layout(mat):
    return [
        [sg.Table(values=mat, justification="center",
                  auto_size_columns=False, enable_events=True, key="-TABLE-")],
        [sg.Button('\u21C7', font="Arial 22", key="-LEFT-"),
         sg.Button('\u21C8', font="Arial 22", key="-UP-"),
         sg.Button('\u21CA', font="Arial 22", key="-DOWN-"),
         sg.Button('\u21C9', font="Arial 22", key="-RIGHT-")],
        [sg.Button("New Game", size=11), sg.Button("Exit", size=11)],
        [sg.Button("Change Theme", size=20)],
        [sg.Button("The game creator's", size=20)]
    ]

def main_window(user_theme, mat):
    sg.theme(user_theme)
    return sg.Window("2048", create_game_layout(mat))

def handle_game_over(mat, user_theme, window):
    choice = sg.popup_yes_no("Game Over!\nStart a new game? (Yes)\nExit (No)")
    if choice == "Yes":
        mat = logic.start_game()
        window["-TABLE-"].update(values=mat)
    else:
        window.close()

def handle_user_input(event, mat, user_theme, window):
    if event in (sg.WIN_CLOSED, "Exit"):
        return False
    elif event in ("-UP-", "-DOWN-", "-LEFT-", "-RIGHT-"):
        direction = event[1:]
        mat, flag = logic.move(mat, direction)
        status = logic.get_current_state(mat)
        print(status)

        if status == 'GAME NOT OVER':
            logic.add_new_2(mat)
        elif status == 'NOT MOVE':
            sg.popup(f"No move {direction.capitalize()}")
        elif status == 'WON':
            sg.popup("YOU WON!")
            logic.add_new_2(mat)
        else:
            handle_game_over(mat, user_theme, window)

    elif event == "New Game":
        mat = logic.start_game()
        window["-TABLE-"].update(values=mat)
    elif event == "The game creator's":
        gui_2048.titles(user_theme)
    elif event == "Change Theme":
        user_theme = gui_2048.theme_select(user_theme)
        window.close()
        sg.theme(user_theme)
        window = main_window(user_theme, mat)
    window["-TABLE-"].update(values=mat)
    return True

if __name__ == '__main__':
    mat = logic.start_game()
    user_theme = "DarkAmber"
    window = main_window(user_theme, mat)

    while True:
        event, values = window.read()
        if not handle_user_input(event, mat, user_theme, window):
            break

window.close()
