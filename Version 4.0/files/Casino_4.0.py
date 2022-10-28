from tkinter import *
import random
import time
import pathlib
from pathlib import *
import colorama
import os

class window():
    def __init__(self, width, height):
        self.master = Tk()
        self.master.geometry(str(width)+"x"+str(height))
        self.master.resizable(width = 0, height = 0)
        self.buttons = []
        self.labels = []
        self.entrys = []
    def button(self, master, x, y, width, height, bg, fg, text, coms, args):
        def callCommands():
            for i in range (0, len(coms)):
                if args[i] == []:
                    coms[i]()
                else:
                    coms[i](*args[i])
        button = Button(master, text=text, bg=bg, fg = fg, command = lambda:[callCommands()])
        button.place(x=x, y=y, width = width, height = height)
        self.buttons.append(button)
    def label(self, master, x, y, width, height, font, bg, fg, text):
        label = Label(master, text = text, font = font, fg = fg, bg = bg, justify = "center")
        label.place(x=x, y=y, width = width, height = height)
        self.labels.append(label)
    def entry(self, master, x, y, width, height, font, bg, fg):
        entry = Entry(master, font = font, fg = fg, bg = bg)
        entry.place(x=x, y=y, width = width, height = height)
        self.entrys.append(entry)

class main():
    def __init__(self):
        self.startkontostand = "200"
        self.win = window(250 ,50)
        self.label = self.win.label(self.win.master, 0, 0, 125, 25,"Calibri", "black", "white", "Ihr Name bitte:")
        self.entry = self.win.entry(self.win.master, 125, 0,125, 25, "Calibri", "black", "white")
        self.button1 = self.win.button(self.win.master, 125, 25, 125, 25, "black", "white", "Login", [self.check_name], [[]])
        self.button2 = self.win.button(self.win.master, 0, 25, 125, 25, "black", "white", "Quit", [self.destroy], [[]])
        self.checkname = None
        self.path = None
        self.namepath = None
        self.kontostand = 0
        self.s = None
    def get_player_name(self):
        return self.win.entrys[0].get()
    def check_name(self):
        self.checkname = str(self.get_player_name())
        #self.path = "C:/Users/Johannes/AppData/Local/Spielstand/" + self.checkname + ".txt"
        if not os.path.exists('game_saves'):
            os.makedirs('game_saves')
        self.path = "game_saves/" + self.checkname + ".txt"
        #self.namepath = Path(self.path)
        self.namepath = Path(self.path)
        if self.checkname == None or self.checkname == "":
            print("Invalid Name")
        else:
            if self.namepath.is_file():
                self.kontostand = self.read_file()
            else:
                myfilec = open(self.path, "w+")
                myfilec.write(self.startkontostand)
                myfilec.close()
                self.kontostand = int(self.startkontostand)
            self.destroy()
            self.s = selection()
    def read_file(self):
        myfile = open(self.path, "r")
        myfiler = myfile.read()
        myfileri = int(myfiler)
        myfile.close()
        return myfileri
    def write_file(self, wert, mode):
        wert1 = self.read_file()
        myfilew = open(self.path, "w")
        if mode:
            endwert = int(wert1)+int(wert)
        else:
            endwert = int(wert1)-int(wert)
        myfilew.write(str(endwert))
        myfilew.close()
        self.update_kontostand()
    def update_kontostand(self):
        self.kontostand = self.read_file()
    def destroy(self):
        self.win.master.destroy()
        

class selection():
    def __init__(self):
        self.win = window(250, 450)
        self.label = self.win.label(self.win.master, 0, 0, 250, 25, "Calibri", "black", "white", "Kontostand: " + str(m.kontostand))
        self.button1 = self.win.button(self.win.master, 0, 25, 125, 125, "black", "white", "Slots", [self.load_game], [["slots"]])
        self.button2 = self.win.button(self.win.master, 125, 25, 125, 125, "black", "white", "Black-Jack", [self.load_game], [["blackjack"]])
        self.button3 = self.win.button(self.win.master, 0, 150, 125, 125, "black", "white", "Roulette", [self.load_game], [["roulette"]])
        self.button4 = self.win.button(self.win.master, 125, 150, 125, 125, "black", "white", "Guess-The-Number", [self.load_game], [["guessthenumber"]])
        self.button5 = self.win.button(self.win.master, 0, 275, 125, 125, "black", "white", "Higher/Lower", [self.load_game], [["higherlower"]])
        for i in range(4):
            self.win.buttons[i+1].config(state="disabled")
        self.button6 = self.win.button(self.win.master, 125, 275, 125, 125, "black", "white", "Chase-The-Button", [self.load_game], [["chasethebutton"]])
        self.button7 = self.win.button(self.win.master, 0, 400, 250, 50, "red", "white", "Quit", [self.destroy], [[]])
    def load_game(self, game):
        if game == "slots":
            m.s = slots()
        elif game == "chasethebutton":
            m.s = chase_the_button()
        self.destroy()
    def destroy(self):
        self.win.master.destroy()
class slots():
    def __init__(self):
        self.win = window(225, 365)
        self.button1 = self.win.button(self.win.master, 0, 0, 112.5, 50, "red", "white", "Quit", [self.destroy], [[]])
        self.button2 = self.win.button(self.win.master, 112.5, 0, 112.5, 50, "black", "white", "Back", [self.back], [[]])
        self.button3 = self.win.button(self.win.master, 0, 50, 225, 50, "black", "white", "Start", [self.start_game], [[]])
        self.jackpot = random.randint(50, 120)
        self.nums = []
        self.labels = []
        self.right = 0
        for j in range(0,3):
            for i in range(0,3):
                self.labels.append(self.win.label(self.win.master, (i*75), 100+(j*75), 75, 75, "Calibri", "black", "white", i))
        for i in range(len(self.win.labels)):
            self.win.labels[i].config(text=i+1)
        self.label1 = self.win.label(self.win.master, 0, 325, 225, 20, "Calbri", "black", "white", "")
        self.label2 = self.win.label(self.win.master, 0, 345, 225, 20, "Calbri", "black", "white", "Kontostand: " + str(m.kontostand))
            
    def start_game(self):
        if int(m.kontostand) < 25:
            self.win.labels[10].config(text="Zu wenig Geld")
            return
        for i in range(0,9):
            self.nums.append(random.randint(1,9))
        for i in range(0,9):
            self.win.labels[i].config(text=self.nums[i], fg="white")
        self.win.labels[9].config(text="")
        for i in range(0,3):
            if self.nums[0+i*3] == self.nums[1+i*3] == self.nums[2+i*3]:
                self.right += 1
                for j in range(0,3):
                    self.win.labels[i*3+j].config(fg="green")
        for i in range(0,3):
            if self.nums[0+i] == self.nums[3+i] == self.nums[6+i]:
                self.right += 1
                self.win.labels[0+i].config(fg="green")
                self.win.labels[3+i].config(fg="green")
                self.win.labels[6+i].config(fg="green")
        if self.nums[0] == self.nums[4] == self.nums[8]:
            self.right += 1
            self.win.labels[0].config(fg="green")
            self.win.labels[4].config(fg="green")
            self.win.labels[8].config(fg="green")
        if self.nums[2] == self.nums[4] == self.nums[6]:
            self.right += 1
            self.win.labels[2].config(fg="green")
            self.win.labels[4].config(fg="green")
            self.win.labels[6].config(fg="green")
        if self.right > 0:
            text = str(self.right) + " Mal gewonnen"
            self.win.labels[9].config(text=text)
            money = self.jackpot * (2**self.right)
            m.write_file(money, True)
        else:
            m.write_file(25, False)
        self.win.labels[10].config(text="Kontostand: " + str(m.kontostand))
        self.right = 0
        self.nums = []
    def back(self):
        m.s = selection()
        self.win.master.destroy()
    def destroy(self):
        self.win.master.destroy()
    def write(self, text):
        return
class chase_the_button():
    def __init__(self):
        self.win = window(300, 300)
        self.button1 = self.win.button(self.win.master, 0, 0, 50, 50, "black", "white", "Back", [self.destroy], [[]])
        self.button2 = self.win.button(self.win.master, 100, 100, 50,50, "black", "white", "Click Me!", [self.click], [[]])
    def click(self):
        x1 = random.randint(50,250)
        y1 = random.randint(50,250)
        self.win.buttons[1].place(x=x1, y=y1)
        m.write_file(2, True)
    def destroy(self):
        m.s = selection()
        self.win.master.destroy()
        
m = main()
m.win.master.mainloop()




