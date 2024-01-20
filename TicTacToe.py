from tkinter import *

#Setting up the main_frame
window = Tk()
window.title('Tic Tac Toe')
window.resizable(False, False)

#Setting up the main frame
main_frame = Frame(window)
main_frame.grid()

click = True


def checker(buttons):
    global click
    if buttons['text'] == ' ' and click == True:
        buttons['text'] = 'X'
        click = False
    elif buttons['text'] == ' ' and click == False:
        buttons['text'] = 'O'
        click = True
    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
          button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        tkMessageBox._show('Results', 'Player X wins')
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        tkMessageBox._show('Results', 'Player O wins')


buttons = StringVar()

#Code execution starts here
#Defining all the buttons
global button1, button2, button3, button4, button5, button6, button7, button8, button9

button1 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button1)})
button1.grid({'row': '0', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button2 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button2)})
button2.grid({'row': '0', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button3 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button3)})
button3.grid({'row': '0', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})


button4 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button4)})
button4.grid({'row': '1', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button5 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button5)})
button5.grid({'row': '1', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button6 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button6)})
button6.grid({'row': '1', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})


button7 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button7)})
button7.grid({'row': '2', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button8 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button8)})
button8.grid({'row': '2', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button9 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button9)})
button9.grid({'row': '2', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})


window.mainloop()