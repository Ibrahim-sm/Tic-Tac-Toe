from tkinter import *
from tkinter import messagebox
import random


def init():
    global turn
    global board
    global counter
    global checklist
    global win_bit
    global computer_bit
    button[0] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(1))
    button[0].grid(column=0, row=1)
    button[1] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(2))
    button[1].grid(column=1, row=1)
    button[2] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(3))
    button[2].grid(column=2, row=1)
    button[3] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(4))
    button[3].grid(column=0, row=2)
    button[4] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(5))
    button[4].grid(column=1, row=2)
    button[5] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(6))
    button[5].grid(column=2, row=2)
    button[6] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(7))
    button[6].grid(column=0, row=3)
    button[7] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(8))
    button[7].grid(column=1, row=3)
    button[8] = Button(board_frame, width=16, height=8, text=' ', font=("Arial", 19), bg='lightgray', cursor='cross',
                       command=lambda: play(9))
    button[8].grid(column=2, row=3)
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    checklist = []
    counter = 0
    turn = 1
    computer_bit = 0
    win_bit = 0
    info.config(font=("Arial", 13),
                text=" Player1 -> X          Player2 -> O          Turn=" + str(turn))
    computer.config(bg='lightgray')


def enable_computer():
    global computer_bit
    if computer_bit == 1:
        computer_bit = 0
        computer.config(bg='lightgray')
    else:
        computer_bit = 1
        computer.config(bg='teal')


def play(a):
    global turn
    global counter
    global board
    global checklist
    global computer_bit
    if turn == 1:
        board[a - 1] = 'X'
        button[a - 1].config(text="X", font=("Arial", 19), bg='teal', state=DISABLED, disabledforeground="white")
        checklist.append(a)
        check()
        if (computer_bit == 1) & (win_bit == 0):
            computer_play()
        else:
            turn = 2
            info.config(font=("Arial", 13),
                        text=" Player1 -> X          Player2 -> O          Turn=" + str(turn))
        counter += 1

    elif turn == 2:
        board[a - 1] = 'O'
        button[a - 1].config(text="O", font=("Arial", 19), bg='teal', state=DISABLED, disabledforeground="white")
        check()
        turn = 1
        info.config(font=("Arial", 13),
                    text=" Player1 -> X          Player2 -> O          Turn=" + str(turn))
        counter += 1


def check():
    if board[0] == board[1] == board[2]:
        win_message(turn, 0, 1, 2)
        return
    elif board[0] == board[3] == board[6]:
        win_message(turn, 0, 3, 6)
        return
    elif board[0] == board[4] == board[8]:
        win_message(turn, 0, 4, 8)
        return
    elif board[1] == board[4] == board[7]:
        win_message(turn, 1, 4, 7)
        return
    elif board[2] == board[5] == board[8]:
        win_message(turn, 2, 5, 8)
        return
    elif board[2] == board[4] == board[6]:
        win_message(turn, 2, 4, 6)
        return
    elif board[3] == board[4] == board[5]:
        win_message(turn, 3, 4, 5)
        return
    elif board[6] == board[7] == board[8]:
        win_message(turn, 6, 7, 8)
        return
    elif counter == 8:
        win_message(0, 0, 0, 0)


def p_random():
    xep = checklist
    r = random.randint(1, 9)
    return p_random() if r in xep else r


def computer_play():
    global turn
    global board
    global counter
    p = p_random()
    checklist.append(p)
    board[p - 1] = 'O'
    button[p - 1].config(text="O", font=("Arial", 19), bg='teal', state=DISABLED, disabledforeground="white")
    counter += 1
    turn = 3
    check()
    turn = 1
    return


def win_message(winner, a, b, c):
    global board
    global counter
    global win_bit
    if winner != 0:
        if winner == 3:
            messagebox.showinfo('Tic-tac-toe', 'Computer Wins!')
        else:
            messagebox.showinfo('Tic-tac-toe', 'Player ' + str(winner) + ' Wins!')
        button[a].config(bg='#660d2c')
        button[b].config(bg='#660d2c')
        button[c].config(bg='#660d2c')
    else:
        messagebox.showinfo('Tic-tac-toe', 'Draw!')
    for i in range(9):
        button[i].config(state=DISABLED)
    win_bit = 1


turn = 1
counter = 0
win_bit = 0
computer_bit = 0
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
checklist = []
top = Tk()
top.configure(background='lightgray')
button = {}
top.title("Tic-tac-toe")
button_frame = Frame(top, bg='lightgray')
button_frame.pack(padx=5, pady=5)
computer = Button(button_frame, font=("Arial", 11), text="Play with a computer", command=lambda: enable_computer())
computer.grid(column=0, row=0, padx=10)
reset = Button(button_frame, font=("Arial", 11), bg='lightgray', text="Play Again", command=lambda: init())
reset.grid(row=0, padx=33, column=2)
info = Label(top, bg='lightgray', font=("Arial", 13),
             text=" Player1 -> X          Player2 -> O          Turn=" + str(turn))
info.pack()
board_frame = Frame(top)
board_frame.pack()
init()

top.mainloop()