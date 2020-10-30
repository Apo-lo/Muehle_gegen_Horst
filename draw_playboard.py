# draw_playboard.py

from tkinter import *
import game_logic as gl

class playboard:
    white_pieces_set = 0
    black_pieces_set = 0
    white_pieces_board = 0
    black_pieces_board = 0
    def __init__(self):
        print("Board erstellt")


board = playboard()


def button_action(x, y):
    gl.button_clicked(board, x, y)

def hilfe():
    print("Hilfe called")

def neustart():
    print("Neustart called")

def generate_window():
    fenster = Tk()
    fenster.title("Mühlebrett")
    fenster.configure(background="light green")
    return fenster


def draw_buttons(fenster):
    board.point_00 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(0,0))
    board.point_03 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(0,3))
    board.point_06 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(0,6))

    board.point_11 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(1,1))
    board.point_13 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(1,3))
    board.point_15 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(1,5))

    board.point_22 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(2,2))
    board.point_23 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(2,3))
    board.point_24 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(2,4))

    board.point_30 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(3,0))
    board.point_31 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(3,1))
    board.point_32 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(3,2))

    board.point_34 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(3,4))
    board.point_35 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(3,5))
    board.point_36 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(3,6))

    board.point_42 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(4,2))
    board.point_43 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(4,3))
    board.point_44 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(4,4))

    board.point_51 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(5,1))
    board.point_53 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(5,3))
    board.point_55 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(5,5))

    board.point_60 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(6,0))
    board.point_63 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(6,3))
    board.point_66 = Button(fenster, text="", bg="brown", activebackground="grey", command=lambda: button_action(6,6))


    '''
    w_01 = Canvas(fenster, width=100, height=100)
    w_01.grid(row=0,column=1)
    w_01.create_line(0, 50, 100, 50)
    w_02 = Canvas(fenster, width=100, height=100)
    w_02.grid(row=0,column=2)
    w_02.create_line(0, 50, 100, 50)
    '''

    # Nun fügen wir die Komponenten unserem Fenster 
    # in der gwünschten Reihenfolge hinzu.
    board.point_00.grid(row=0, column=0, padx=20, pady=20)
    board.point_03.grid(row=0, column=3, padx=20, pady=20)
    board.point_06.grid(row=0, column=6, padx=20, pady=20)
    board.point_11.grid(row=1, column=1, padx=20, pady=20)
    board.point_13.grid(row=1, column=3, padx=20, pady=20)
    board.point_15.grid(row=1, column=5, padx=20, pady=20)
    board.point_22.grid(row=2, column=2, padx=20, pady=20)
    board.point_23.grid(row=2, column=3, padx=20, pady=20)
    board.point_24.grid(row=2, column=4, padx=20, pady=20)
    board.point_30.grid(row=3, column=0, padx=20, pady=20)
    board.point_31.grid(row=3, column=1, padx=20, pady=20)
    board.point_32.grid(row=3, column=2, padx=20, pady=20)
    board.point_34.grid(row=3, column=4, padx=20, pady=20)
    board.point_35.grid(row=3, column=5, padx=20, pady=20)
    board.point_36.grid(row=3, column=6, padx=20, pady=20)
    board.point_42.grid(row=4, column=2, padx=20, pady=20)
    board.point_43.grid(row=4, column=3, padx=20, pady=20)
    board.point_44.grid(row=4, column=4, padx=20, pady=20)
    board.point_51.grid(row=5, column=1, padx=20, pady=20)
    board.point_53.grid(row=5, column=3, padx=20, pady=20)
    board.point_55.grid(row=5, column=5, padx=20, pady=20)
    board.point_60.grid(row=6, column=0, padx=20, pady=20)
    board.point_63.grid(row=6, column=3, padx=20, pady=20)
    board.point_66.grid(row=6, column=6, padx=20, pady=20)

    board.info1 = Label(fenster, text="Bitte Stein setzen!")
    board.info1.grid(row=7, column=0)
    board.info2 = Label(fenster, text="")
    board.info2.grid(row=8, column=0)

    menuleiste = Menu(fenster)
    datei_menu = Menu(menuleiste, tearoff=0)
    datei_menu.add_command(label="Hilfe", command=hilfe)
    datei_menu.add_command(label="Neustart", command=neustart)
    datei_menu.add_command(label="Schließen", command=fenster.quit)

    menuleiste.add_cascade(label="Datei", menu=datei_menu)
    fenster.config(menu=menuleiste)

    fenster.mainloop()