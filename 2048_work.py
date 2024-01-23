
import logic
import PySimpleGUI as sg

if __name__ == '__main__':
	mat = logic.start_game()
	sg.theme("DarkAmber")
	layout = [[sg.Table(values=mat, headings=["Col1", "Col2", "Col3", "Col4"], justification="center",
						num_rows=4, row_height=70, key="-TABLE-")],
			[sg.Button('\u21C7', font="Arial 20", key ="-LEFT-"),
			 sg.Button('\u21C8', font="Arial 20", key ="-UP-"), 
			 sg.Button('\u21CA', font="Arial 20", key ="-DOWN-"), 
			 sg.Button('\u21C9', font="Arial 20", key ="-RIGHT-")],
        	[sg.Button("New Game", size=14), sg.Button("Exit", size=14)]
	]
	window = sg.Window("2048", layout)

while(True):
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == "Exit":
		break
	elif event == "-UP-":
		# call the move_up function
		mat, flag = logic.move_up(mat)
		# get the current state
		status = logic.get_current_state(mat)
		print(status)
		# if game not over then continue
		# and add a new two
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		elif (status == 'NOT MOVE'):
			sg.popup("  No move Up  ")
			continue
		elif (status == 'WON'):
			sg.popup("  YUO WON !!! ")
			logic.add_new_2(mat)
		# else break the loop 
		else:
			choice = sg.popup_yes_no("  Game Over!\n Start a new game? (Yes)\n   Exit (No)")
			if choice == "Yes":
				mat = logic.start_game()
				window["-TABLE-"].update(values=mat)
				continue
			else:
				break
	elif event == "-DOWN-":
		# to move down
		mat, flag = logic.move_down(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		elif (status == 'NOT MOVE'):
			sg.popup("  No move Down  ")
			continue
		elif (status == 'WON'):
			sg.popup("  YUO WON !!! ")
			logic.add_new_2(mat)
		else:
			choice = sg.popup_yes_no("  Game Over!\n Start a new game? (Yes)\n   Exit (No)")
			if choice == "Yes":
				mat = logic.start_game()
				window["-TABLE-"].update(values=mat)
				continue
			else:
				break
	elif event == "-LEFT-":
		# to move left
		mat, flag = logic.move_left(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		elif (status == 'NOT MOVE'):
			sg.popup("  No move Left  ")
			continue
		elif (status == 'WON'):
			sg.popup("  YUO WON !!! ")
			logic.add_new_2(mat)
		else:
			choice = sg.popup_yes_no("  Game Over!\n Start a new game? (Yes)\n   Exit (No)")
			if choice == "Yes":
				mat = logic.start_game()
				window["-TABLE-"].update(values=mat)
				continue
			else:
				break
	elif event == "-RIGHT-":
		# to move right
		mat, flag = logic.move_right(mat)
		status = logic.get_current_state(mat)
		print(status)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		elif (status == 'NOT MOVE'):
			sg.popup("  No move Right  ")
			continue
		elif (status == 'WON'):
			sg.popup("  YUO WON !!! ")
			logic.add_new_2(mat)
		else:
			choice = sg.popup_yes_no("  Game Over!\n Start a new game? (Yes)\n   Exit (No)")
			if choice == "Yes":
				mat = logic.start_game()
				window["-TABLE-"].update(values=mat)
				continue
			else:
				break
	elif event == "New Game":
		mat = logic.start_game()
		window["-TABLE-"].update(values=mat)
		continue

	window["-TABLE-"].update(values=mat)
	for list in mat:
		print(list)
window.close()
