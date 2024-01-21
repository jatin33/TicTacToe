from tkinter import *
import logic

#Setting up the main_frame
window = Tk()
window.title('Tic Tac Toe')
window.geometry("250x250")
window.resizable(False, False)

#Setting up the main frame
main_frame = Frame(window)
main_frame.grid()

#Defining the frame that is going to hold the win or end of he game message
#and has a restart button
message_frame = Frame(window) 


#Code execution starts here
#setting up key bindings
window.bind("7", lambda event: logic.checker(1, button_list, main_frame, message_frame, message))
window.bind("8", lambda event: logic.checker(2, button_list, main_frame, message_frame, message))
window.bind("9", lambda event: logic.checker(3, button_list, main_frame, message_frame, message))
window.bind("4", lambda event: logic.checker(4, button_list, main_frame, message_frame, message))
window.bind("5", lambda event: logic.checker(5, button_list, main_frame, message_frame, message))
window.bind("6", lambda event: logic.checker(6, button_list, main_frame, message_frame, message))
window.bind("1", lambda event: logic.checker(7, button_list, main_frame, message_frame, message))
window.bind("2", lambda event: logic.checker(8, button_list, main_frame, message_frame, message))
window.bind("3", lambda event: logic.checker(9, button_list, main_frame, message_frame, message))
#Defining all the buttons in main_frame

button1 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(1, button_list, main_frame, message_frame, message)})
button1.grid({'row': '0', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button2 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(2, button_list, main_frame, message_frame, message)})
button2.grid({'row': '0', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button3 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(3, button_list, main_frame, message_frame, message)})
button3.grid({'row': '0', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})


button4 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(4, button_list, main_frame, message_frame, message)})
button4.grid({'row': '1', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button5 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(5, button_list, main_frame, message_frame, message)})
button5.grid({'row': '1', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button6 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(6, button_list, main_frame, message_frame, message)})
button6.grid({'row': '1', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})


button7 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(7, button_list, main_frame, message_frame, message)})
button7.grid({'row': '2', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button8 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(8, button_list, main_frame, message_frame, message)})
button8.grid({'row': '2', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button9 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: logic.checker(9, button_list, main_frame, message_frame, message)})
button9.grid({'row': '2', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})

#Defining a list to reference the buttons
button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

#Defining the widgets in the message_frame
#The message label
message = Label(message_frame, text=" ", font=("Arial", 20))
message.grid()

#The restart button
restart_button = Button(message_frame, text = "Restart", command=lambda: logic.restart(button_list, message_frame, main_frame))
restart_button.grid()

window.mainloop()