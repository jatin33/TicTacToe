from tkinter import *

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

#This variable determine the turn of who X or O
turn = "X"

#Fonction to check if their is a winner so far or after all the buttons all filled with X, O.
#This fonction is intended to be called everytime a player plays.
def is_winner():
    #Getting all button text and appending it to a list
    plays = [button["text"] for button in button_list]
    #Cecking if there a win, according to 8 cases of win and if their is a winner
    #return it
    if plays[0] == plays[1] == plays[2]:
        return plays[0]
    elif plays[3] == plays[4] == plays[5]:
        return plays[3]
    elif plays[6] == plays[7] == plays[8]:
        return plays[6]
    elif plays[0] == plays[3] == plays[6]:
        return plays[0]
    elif plays[1] == plays[4] == plays[7]:
        return plays[1]
    elif plays[2] == plays[5] == plays[8]:
        return plays[2]
    elif plays[0] == plays[4] == plays[8]:
        return plays[0]
    elif plays[6] == plays[4] == plays[2]:
        return plays[6]
    
    #Checking if the grid is full to stop the game
    if " " not in plays:
        return "no winner"

#Fonction to check which button is clicked and update it's text with X or O
def checker(button_number):
    #Setting the variable turn to global because it's outside this fonction
    global turn
    #determining button index from the list
    button_index = button_number - 1
    #referencing the button using button index
    button = button_list[button_index]
    #getting the button text
    button_text = button["text"]
    
    #Checking the button text if it's empty then change it's text to X or O
    if button_text == " ":
        #Checking if it's the turn of X or O
        if turn == "X":
            button.config(text = "X")
            #Changing the turn to O, Next time O will play
            turn = "O"
        else:
            button.config(text = "O")
            #Changing the turn to X, Next time X will play
            turn = "X"
    #If text is already filled with X or O in the button, then return pass
    else:
        pass
    #Calling a fonction to check who is the winner or if their is a winner so far
    winner = is_winner()
    
    if winner == "X" or winner == "O":
        #hiding the main_frame
        main_frame.grid_forget()
        #showing the message_frame
        message_frame.grid()
        #Setting up the the message label text
        message.config(text = f"The winner is {winner}")
    elif winner == "no winner":
        #hiding the main_frame
        main_frame.grid_forget()
        #showing the message_frame
        message_frame.grid()
        #Setting up the the message label text
        message.config(text = "There is no winner")

#Restart fonction, to restart the game
def restart():
    #reseting buttons text to " "
    for button in button_list:
        button.config(text = " ")
    #Hiding message frame
    message_frame.grid_forget()
    #Showing the main frame
    main_frame.grid()

#Code execution starts here
#setting up key bindings
window.bind("7", lambda event: checker(1))
window.bind("8", lambda event: checker(2))
window.bind("9", lambda event: checker(3))
window.bind("4", lambda event: checker(4))
window.bind("5", lambda event: checker(5))
window.bind("6", lambda event: checker(6))
window.bind("1", lambda event: checker(7))
window.bind("2", lambda event: checker(8))
window.bind("3", lambda event: checker(9))
#Defining all the buttons in main_frame

button1 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(1)})
button1.grid({'row': '0', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button2 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(2)})
button2.grid({'row': '0', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button3 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(3)})
button3.grid({'row': '0', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})


button4 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(4)})
button4.grid({'row': '1', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button5 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(5)})
button5.grid({'row': '1', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button6 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(6)})
button6.grid({'row': '1', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})


button7 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(7)})
button7.grid({'row': '2', 'column': '0', 'sticky': 'NSEW', 'in': main_frame})


button8 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(8)})
button8.grid({'row': '2', 'column': '1', 'sticky': 'NSEW', 'in': main_frame})


button9 = Button(main_frame, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(9)})
button9.grid({'row': '2', 'column': '2', 'sticky': 'NSEW', 'in': main_frame})

#Defining a list to reference the buttons
button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

#Defining the widgets in the message_frame
#The message label
message = Label(message_frame, text=" ", font=("Arial", 20))
message.grid()

#The restart button
restart_button = Button(message_frame, text = "Restart", command=restart)
restart_button.grid()

window.mainloop()