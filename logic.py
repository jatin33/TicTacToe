from tkinter import *

#This variable determine the turn of who X or O
turn = "X"

#Fonction to check if their is a winner so far or after all the buttons all filled with X, O.
#This fonction is intended to be called everytime a player plays.
def is_winner(button_list):
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
def checker(button_number, button_list, main_frame, message_frame, message):
    global turn
    #Setting the variable turn to global because it's outside this fonction
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
    winner = is_winner(button_list)
    
    #Checking the variable winner that is returned after calling is_winner()
    #If X or O won, switching the screen and indicate the winner
    if winner == "X" or winner == "O":
        #hiding the main_frame
        main_frame.grid_forget()
        #showing the message_frame
        message_frame.grid()
        #Setting up the the message label text
        message.config(text = f"The winner is {winner}")
        
    elif winner == "no winner":
        #If there is no winner, switch the screen and indicate that
        #hiding the main_frame
        main_frame.grid_forget()
        #showing the message_frame
        message_frame.grid()
        #Setting up the the message label text
        message.config(text = "There is no winner")

#Restart fonction, to restart the game
def restart(button_list, message_frame, main_frame):
    global turn
    #reseting buttons text to " "
    for button in button_list:
        button.config(text = " ")
    #reseting turns
    turn = "X"
    #Hiding message frame
    message_frame.grid_forget()
    #Showing the main frame
    main_frame.grid()