import PySimpleGUI as sg


def titles(user_theme):
	sg.theme(user_theme)
	layout = [[sg.Text("Game Director: Jolita Visockaitė", pad=((5,0), (20,0)))],
              [sg.Text("Main Programer: Evaldas Gegeckas")],
			  [sg.Text("Main Disigner: Martynas Pupkus")],
			  [sg.Text("Main 2D Animator: Aivaras Minkevicius")],
			  [sg.Text("Special Thank's to: Poltorak Anton")],
		      [sg.Button("Close", size=11, pad=((90,10), (30,0)))]
	]
	window = sg.Window("2048", layout)
	while(True):
		event, values = window.read()
		if event == sg.WIN_CLOSED or event == "Close":
			break
	window.close()

def theme_select(user_theme):
    sg.theme(user_theme)
    themes = sg.theme_list()

    layout = [
        [sg.Table(values=[[str(i)]+[(themes[i-1])] for i in range(1, len(themes))],
                  headings=["Number", "Theme"], auto_size_columns=True,
                 justification="center", num_rows=min(25, len(themes)),
                  key="-TABLE-", enable_events=True)],
        [sg.Button("Apply and Exit", size=15), sg.Button("Exit", size=15)]
    ]

    window = sg.Window("Table of Themes", layout, resizable=True)
    changed_theme = user_theme

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window.close()
            return user_theme
        elif event == "Apply and Exit":
             window.close()
             return changed_theme
        elif event == "-TABLE-":
            window.hide()
            creat_window(themes[values["-TABLE-"][0]])
            window.un_hide()
            changed_theme = themes[values["-TABLE-"][0]]


def creat_window(theme):
    sg.theme(theme)
    layout = [[sg.Text(f'This is example of "{theme}" theme')],
              [sg.InputText()],
              [sg.Button("Close example")],
              [sg.Text(f'    Theme - "{theme}"', font= "Arial 20")]]
    window = sg.Window("Example", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close example":
        window.close()
