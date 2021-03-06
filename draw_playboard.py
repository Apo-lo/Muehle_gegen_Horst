# draw_playboard.py

from tkinter import *
import random
import game_logic as gl
import socket

globalwindow = None

class playboard:
    def __init__(self):
        self.human_pieces_set = 0
        self.cpu_pieces_set = 0
        self.human_pieces_board = 0
        self.cpu_pieces_board = 0
        self.remove_piece = False
        self.move_piece = False
        self.jump_piece = False
        self.moved_x = 0
        self.moved_y = 0
        self.win = 0
        self.human_is = "white"
        self.cpu_is = "black"
        self.neutral_color = "brown"
        self.move_color = "blue"
        self.connect_to_unity = False
        self.host = "127.0.0.1"
        self.port = 25001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Board erstellt")


def button_action(board,x, y):
    gl.button_clicked(board, x, y)


def hilfe():
    print("Hilfe called")


def neustart():
    print("Neustart called")
    beenden()
    window = generate_window()
    board = playboard()
    draw_buttons(board, window)


def beenden():
    global globalwindow
    print("Beenden called")
    globalwindow.destroy()


def generate_window():
    global globalwindow
    window = Tk()
    window.title("Mühlebrett")
    window.configure(background="light green")
    globalwindow = window
    return window


def draw_buttons(board, window):
    board.point_00 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,0,0))
    board.point_00.x = 0
    board.point_00.y = 0
    board.point_03 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,0,3))
    board.point_03.x = 0
    board.point_03.y = 3
    board.point_06 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,0,6))
    board.point_06.x = 0
    board.point_06.y = 6

    board.point_11 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,1,1))
    board.point_11.x = 1
    board.point_11.y = 1
    board.point_13 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,1,3))
    board.point_13.x = 1
    board.point_13.y = 3
    board.point_15 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,1,5))
    board.point_15.x = 1
    board.point_15.y = 5

    board.point_22 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,2,2))
    board.point_22.x = 2
    board.point_22.y = 2
    board.point_23 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,2,3))
    board.point_23.x = 2
    board.point_23.y = 3
    board.point_24 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,2,4))
    board.point_24.x = 2
    board.point_24.y = 4

    board.point_30 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,3,0))
    board.point_30.x = 3
    board.point_30.y = 0
    board.point_31 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,3,1))
    board.point_31.x = 3
    board.point_31.y = 1    
    board.point_32 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,3,2))
    board.point_32.x = 3
    board.point_32.y = 2

    board.point_34 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,3,4))
    board.point_34.x = 3
    board.point_34.y = 4
    board.point_35 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,3,5))
    board.point_35.x = 3
    board.point_35.y = 5
    board.point_36 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,3,6))
    board.point_36.x = 3
    board.point_36.y = 6

    board.point_42 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,4,2))
    board.point_42.x = 4
    board.point_42.y = 2
    board.point_43 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,4,3))
    board.point_43.x = 4
    board.point_43.y = 3
    board.point_44 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,4,4))
    board.point_44.x = 4
    board.point_44.y = 4

    board.point_51 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,5,1))
    board.point_51.x = 5
    board.point_51.y = 1
    board.point_53 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,5,3))
    board.point_53.x = 5
    board.point_53.y = 3
    board.point_55 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,5,5))
    board.point_55.x = 5
    board.point_55.y = 5

    board.point_60 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,6,0))
    board.point_60.x = 6
    board.point_60.y = 0    
    board.point_63 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,6,3))
    board.point_63.x = 6
    board.point_63.y = 3    
    board.point_66 = Button(window, text="", bg=board.neutral_color, height = 2, width = 4, activebackground="grey", command=lambda: button_action(board,6,6))
    board.point_66.x = 6
    board.point_66.y = 6


    '''
    w_01 = Canvas(window, width=100, height=100)
    w_01.grid(row=0,column=1)
    w_01.create_line(0, 50, 100, 50)
    w_02 = Canvas(window, width=100, height=100)
    w_02.grid(row=0,column=2)
    w_02.create_line(0, 50, 100, 50)
    '''

    # Nun fügen wir die Komponenten unserem Fenster 
    # in der gewünschten Reihenfolge hinzu.
    board.point_00.grid(row=0, column=0, padx=23, pady=20)
    board.point_03.grid(row=0, column=3, padx=23, pady=20)
    board.point_06.grid(row=0, column=6, padx=23, pady=20)
    board.point_11.grid(row=1, column=1, padx=23, pady=20)
    board.point_13.grid(row=1, column=3, padx=23, pady=20)
    board.point_15.grid(row=1, column=5, padx=23, pady=20)
    board.point_22.grid(row=2, column=2, padx=23, pady=20)
    board.point_23.grid(row=2, column=3, padx=23, pady=20)
    board.point_24.grid(row=2, column=4, padx=23, pady=20)
    board.point_30.grid(row=3, column=0, padx=23, pady=20)
    board.point_31.grid(row=3, column=1, padx=23, pady=20)
    board.point_32.grid(row=3, column=2, padx=23, pady=20)
    board.point_34.grid(row=3, column=4, padx=23, pady=20)
    board.point_35.grid(row=3, column=5, padx=23, pady=20)
    board.point_36.grid(row=3, column=6, padx=23, pady=20)
    board.point_42.grid(row=4, column=2, padx=23, pady=20)
    board.point_43.grid(row=4, column=3, padx=23, pady=20)
    board.point_44.grid(row=4, column=4, padx=23, pady=20)
    board.point_51.grid(row=5, column=1, padx=23, pady=20)
    board.point_53.grid(row=5, column=3, padx=23, pady=20)
    board.point_55.grid(row=5, column=5, padx=23, pady=20)
    board.point_60.grid(row=6, column=0, padx=23, pady=20)
    board.point_63.grid(row=6, column=3, padx=23, pady=20)
    board.point_66.grid(row=6, column=6, padx=23, pady=20)

    board.info1 = Label(window, text="Bitte Stein setzen!")
    board.info1.grid(row=7, columnspan = 7)
    board.info2 = Label(window, text="")
    board.info2.grid(row=8, columnspan = 7)

    menuleiste = Menu(window)
    datei_menu = Menu(menuleiste, tearoff=0)
    datei_menu.add_command(label="Hilfe", command=hilfe)
    datei_menu.add_command(label="Neustart", command=neustart)
    datei_menu.add_command(label="Schließen", command=beenden)

    menuleiste.add_cascade(label="Datei", menu=datei_menu)
    window.config(menu=menuleiste)

    # check if human or cpu begins
    if(random.randint(0,1) == 0):
        board.human_is = "black"
        board.cpu_is = "white"
        gl.computers_turn(board)
    
    window.mainloop()