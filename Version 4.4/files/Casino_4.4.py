from tkinter import *
from tkinter import ttk
import random
import time
import pathlib
from pathlib import *
import time
import os 


class window():
    def __init__(self, width, height):
        self.master = Tk()
        self.master.geometry(str(width)+"x"+str(height) + "+100+100" )
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

class Main():
    def __init__(self):
        self.startkontostand = "200"
        self.win = window(250 ,50)
        self.label = self.win.label(self.win.master, 0, 0, 125, 25,"Calibri", "black", "white", "Your Name:")
        self.entry = self.win.entry(self.win.master, 125, 0,125, 25, "Calibri", "black", "white")
        self.button1 = self.win.button(self.win.master, 125, 25, 125, 25, "black", "white", "Login", [self.check_name], [[]])
        self.button2 = self.win.button(self.win.master, 0, 25, 125, 25, "black", "white", "Quit", [self.destroy], [[]])
        self.checkname = None
        self.path = None
        self.namepath = None
        self.kontostand = 0
        self.s = None
        self.running = True
    def get_kontostand(self):
        self.update_kontostand()
        return self.kontostand
    def get_player_name(self):
        return self.win.entrys[0].get()
    def check_name(self):
        self.checkname = str(self.get_player_name())
        if not os.path.exists('game_saves'):
            os.makedirs('game_saves')
        self.path = "game_saves/" + self.checkname + ".txt"
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
        self.running = False
        self.win.master.destroy()
        
class selection():
    def __init__(self):
        self.win = window(250, 450)
        self.label = self.win.label(self.win.master, 0, 0, 250, 25, "Calibri", "black", "white", "Money: " + str(m.get_kontostand()))
        self.button1 = self.win.button(self.win.master, 0, 25, 125, 125, "black", "white", "Slots", [self.load_game], [["slots"]])
        self.button2 = self.win.button(self.win.master, 125, 25, 125, 125, "black", "white", "Black-Jack", [self.load_game], [["blackjack"]])
        self.button3 = self.win.button(self.win.master, 0, 150, 125, 125, "black", "white", "Roulette", [self.load_game], [["roulette"]])
        self.button4 = self.win.button(self.win.master, 125, 150, 125, 125, "black", "white", "Guess-The-Number", [self.load_game], [["guessthenumber"]])
        self.button5 = self.win.button(self.win.master, 0, 275, 125, 125, "black", "white", "Higher/Lower", [self.load_game], [["higherlower"]])
        self.button6 = self.win.button(self.win.master, 125, 275, 125, 125, "black", "white", "Chase-The-Button", [self.load_game], [["chasethebutton"]])
        self.button7 = self.win.button(self.win.master, 0, 400, 250, 50, "red", "white", "Quit", [self.destroy], [[]])
    def load_game(self, game):
        if game == "slots":
            m.s = slots()
        elif game == "chasethebutton":
            m.s = chase_the_button()
        elif game == "higherlower":
            m.s = higher_lower()
        elif game == "guessthenumber":
            m.s = guessthenumber()
        elif game == "blackjack":
            m.s = blackjack()
        elif game == "roulette":
            m.s = roulette()
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
        self.label2 = self.win.label(self.win.master, 0, 345, 225, 20, "Calbri", "black", "white", "Money: " + str(m.kontostand))
            
    def start_game(self):
        if int(m.get_kontostand()) < 25:
            self.win.labels[10].config(text="No Money!!!", fg="red")
            return
        for i in range(0,9):
            self.nums.append(random.randint(1,9))
        for i in range(0,9):
            self.win.labels[i].config(text=self.nums[i], fg="white")
        self.win.labels[9].config(text="", fg="white")
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
            text = str(self.right) + "x Win!!"
            self.win.labels[9].config(text=text, fg="green")
            money = self.jackpot * (2**self.right)
            m.write_file(money, True)
        else:
            m.write_file(25, False)
        self.win.labels[10].config(text="Money: " + str(m.get_kontostand()))
        self.right = 0
        self.nums = []
    def back(self):
        m.s = selection()
        self.win.master.destroy()
    def destroy(self):
        self.win.master.destroy()

class blackjack():
    def __init__(self):
        self.win = window(250,325)
        self.button1 = self.win.button(self.win.master, 0, 0, 125, 50, "red", "white", "Quit", [self.destroy], [[]])
        self.button2 = self.win.button(self.win.master, 125, 0, 125, 50, "black", "white", "Back", [self.back], [[]])
        self.button3 = self.win.button(self.win.master, 0, 75, 250, 50, "black", "white", "Start", [self.start_game], [[]])
        self.button4 = self.win.button(self.win.master, 0, 125, 125, 50, "black", "white", "1 More Card", [self.m_Karten], [[False]])
        self.button5 = self.win.button(self.win.master, 125, 125, 125, 50, "black", "white", "No More Card", [self.check], [[]])
        self.label1 = self.win.label(self.win.master, 0, 50, 125, 25, "Calibri", "black", "white", "Insert Money: ")
        self.label2 = self.win.label(self.win.master, 0, 175, 250, 100, "Calibri", "black", "white", "")
        self.label3 = self.win.label(self.win.master, 0, 275, 250, 25, "Calibri", "black", "white", "")
        self.label4 = self.win.label(self.win.master, 0, 300, 250, 25, "Calibri", "black", "white", "Money: " + str(m.kontostand))
        self.entry1 = self.win.entry(self.win.master, 125, 50, 125, 25, "Calibri", "black", "white")
        self.win.entrys[0].config(justify="center")
        self.win.buttons[3].config(state="disabled")
        self.win.buttons[4].config(state="disabled")
        self.set = 0
        self.symbole = ["Ass","King","Queen","Bube","10","9","8","7","6","5","4","3","2"]
        self.farben = ["Karo","Herz","Pik","Kreuz"]
        self.Karten = []
        self.mKarten = []
        self.gKarten = []
        self.mWert = 0
        self.gWert = 0
        for f in self.symbole:
            for s in self.farben:
                self.Karten.append([f, s])
    def check(self):
        self.win.buttons[3].config(state="disabled")
        self.win.buttons[4].config(state="disabled")
        if self.mWert > 21:
            m.write_file(self.set, False)
            self.win.labels[2].config(text="Fail!", fg = "red")
        elif self.mWert == 21 and len(self.mKarten) == 2:
            m.write_file(self.set*2.5, True)
            self.win.labels[2].config(text="Black-Jack", fg="green")
        elif self.gWert == 21 and len(self.gKarten) == 2:
            m.write_file(self.set, False)
            self.win.labels[2].config(text="Enemy has Black-Jack", fg="red")
        elif self.gWert > 21:
            m.write_file(self.set*2, True)
            self.win.labels[2].config(text="Enemy Failed! ", fg="green")
        elif self.mWert == self.gWert:
            m.write_file(self.set, False)
            self.win.labels[2].config(text="Fail!", fg="red")
        elif self.mWert < self.gWert:
            m.write_file(self.set, False)
            self.win.labels[2].config(text="Fail", fg="red")
        elif self.mWert > self.gWert:
            m.write_file(self.set*2, True)
            self.win.labels[2].config(text="Win!", fg="green")
        else:
            self.win.labels[2].config(text=str(self.mWert) + str(self.gWert))
        self.win.labels[3].config(text="Money: " + str(m.kontostand))
    def restart_game(self):
        self.destroy()
        m.s = blackjack()
    def start_game(self):
        self.button3 = self.win.button(self.win.master, 0, 75, 250, 50, "black", "white", "Play Again", [self.restart_game], [[]])
        self.win.buttons[3].config(state="active")
        self.win.buttons[4].config(state="active")
        try:
            set = int(self.win.entrys[0].get())
            self.set = set
        except ValueError:
            self.set = 1
        self.win.entrys[0].destroy()
        del self.win.entrys[0]
        self.win.labels[0].place(x=0, width = 250)
        self.win.labels[0].config(text="Set Money: " + str(self.set))
        random.shuffle(self.Karten)
        for i in range(2):
            self.m_Karten(False)
        for i in range(2):
            self.m_Karten(True)
        if self.gWert < 17:
            self.m_Karten(True)
    def m_Karten(self, player):
        if len(self.mKarten) >= 10:
            self.check()
            self.win.buttons[3].config(state="disabled")
            return
        card = (self.Karten.pop())
        if player:
            self.gKarten.append(card)
            self.gWert += self.wert(card)
        else:
            self.mKarten.append(card)
            self.mWert += self.wert(card)
            self.win.labels[1].config(text="Cards: \n" + self.get_m_cards()[0])
    def get_m_cards(self):
        rere = ""
        ini = 1
        for card in self.mKarten:
            if ini % 3 == 0:
                if rere == "":
                    rere += card[1] + " " + card[0]
                else:
                    rere += ", " + card[1] + " " + card[0] + "\n"
            else:
                if rere == "":
                    rere += card[1] + " " + card[0]
                else:
                    if ini % 3 == 1:
                        rere += card[1] + " " + card[0]
                    else:
                        rere += ", " + card[1] + " " + card[0]
            ini += 1
        return [str(rere)]
    def wert(self, wert):
        if wert[0] == "Ass":
            return 11
        elif wert[0] in self.symbole[1:4]:
            return 10
        else:
            return int(wert[0])
    def back(self):
        m.s = selection()
        self.destroy()
    def destroy(self):
        self.win.master.destroy()

class roulette():
    def __init__(self):
        self.win = window(250,260)
        self.button1 = self.win.button(self.win.master, 0, 0, 125, 50, "red", "white", "Quit", [self.destroy], [[]])
        self.button2 = self.win.button(self.win.master, 125, 0, 125, 50, "black", "white", "Back", [self.back], [[]])
        self.button3 = self.win.button(self.win.master, 0, 50, 250, 50, "black", "white", "Start", [self.start_game], [[]])
        self.combobox = ttk.Combobox(self.win.master, values=["Black", "Red", "High", "Low", "Even", "Odd", "1. Dozen", "2. Dozen", "3. Dozen", "1. Column", "2. Column", "3. Column", "Plein"])
        self.combobox.place(x=0, y=125, width=250)
        self.slider = Scale(self.win.master, from_=0, to=36, orient=HORIZONTAL, bg="black", fg="white")
        self.slider.place(x=0, y=145, width=250)
        self.label1 = self.win.label(self.win.master, 0, 185, 250, 25, "Calibri", "black", "white", "")
        self.label2 = self.win.label(self.win.master, 0, 210, 250, 25, "Calibri", "black", "white", "")
        self.label3 = self.win.label(self.win.master, 0, 235, 250, 25, "Calibri", "black", "white", "Money: " + str(m.kontostand))
        self.label4 = self.win.label(self.win.master, 0, 100, 125, 25, "Calibri", "black", "white", "Insert Money: ")
        self.entry1 = self.win.entry(self.win.master, 125, 100, 125, 25, "Calibri", "black", "white")
        self.win.entrys[0].config(justify="center")
        self.number = 0
        self.black = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        self.red = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        self.selection = None
        self.set = 0
    def restart_game(self):
        self.destroy()
        m.s = roulette()
    def start_game(self):
        try:
            set = int(self.win.entrys[0].get())
            self.set = set
        except ValueError:
            self.set = 1
        self.win.labels[3].config(text="Set Money: " + str(self.set))
        self.win.labels[0].config(text="")
        self.number = random.randint(0,36)
        self.selection = self.combobox.get()
        if self.selection == "":
            self.win.labels[0].config(text="Nothing Selected!", fg="yellow")
        elif (self.selection == "Black") and (self.number in self.black):
            m.write_file(self.set, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif (self.selection == "Red") and (self.number in self.red):
            m.write_file(self.set, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "High" and self.number >= 19:
            m.write_file(self.set, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "Low" and self.number <= 18 and self.number != 0:
            m.write_file(self.set, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "Even" and self.number % 2 == 0 and self.number != 0:
            m.write_file(self.set, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "Odd" and self.number % 2 != 0 and self.number != 0:
            m.write_file(self.set, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "1. Dozen" and self.number <= 12 and self.number != 0:
            m.write_file(self.set*2, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "2. Dozen" and self.number > 12 and self.number <= 24:
            m.write_file(self.set*2, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "3. Dozen" and self.number > 24:
            m.write_file(self.set*2, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "1. Column" and (((self.number - 1)%3 == 0 )or (self.number == 1)):
            m.write_file(self.set*2, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "2. Column" and (self.number + 1)%3 == 0:
            m.write_file(self.set*2, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "3. Column" and self.number %3 == 0:
            m.write_file(self.set*2, True)
            self.win.labels[0].config(text="Win!", fg="green")
        elif self.selection == "Plein" and int(self.slider.get()) == self.number:
            m.write_file(self.set*35, True)
            self.win.labels[0].config(text="Win!", fg="green")
        else:
            self.win.labels[0].config(text="Fail!", fg="red")
            m.write_file(self.set, False)
        self.win.labels[1].config(text="Number: " + str(self.number))
        self.win.labels[2].config(text="Money: " + str(m.kontostand))
    def back(self):
        m.s = selection()
        self.destroy()
    def destroy(self):
        self.win.master.destroy()

class guessthenumber():
    def __init__(self):
        self.win = window(250, 185)
        self.button1 = self.win.button(self.win.master, 0, 0, 125, 50, "red", "white", "Quit", [self.destroy], [[]])
        self.button2 = self.win.button(self.win.master, 125, 0, 125, 50, "black", "white", "Back", [self.back], [[]])
        self.button3 = self.win.button(self.win.master, 0, 85, 250, 50, "black", "white", "Start", [self.start_game], [[]])
        self.slider = Scale(self.win.master, from_=1, to=100, orient=HORIZONTAL, bg="black", fg="white")
        self.slider.place(x=0, y=50, width=250)
        self.label1 = self.win.label(self.win.master, 0, 135, 250, 25, "Calibri", "black", "white", "")
        self.label2 = self.win.label(self.win.master, 0, 160, 250, 25, "Calibri", "black", "white", "Money: " + str(m.get_kontostand()))
        self.number = 0
        self.guess = 0
        self.jackpot = random.randint(250, 400)
    def start_game(self):
        if m.get_kontostand() < 3:
            self.win.labels[1].config(text="No Money!!!", fg="red")
            return
        self.win.labels[0].config(text="")
        self.number = random.randint(1,100)
        self.guess = self.slider.get()
        if self.number == self.guess:
            self.win.labels[0].config(text="Win!", fg="green")
            self.win.labels[1].config(text="Money: " + str(m.get_kontostand()))
            m.write_file(self.jackpot, True)
            self.jackpot = random.randint(250, 400)
        else:
            self.win.labels[0].config(text="Fail! Number: " + str(self.number), fg="red")
            self.win.labels[1].config(text="Money: " + str(m.get_kontostand()))
            m.write_file(3, False)
            self.jackpot += 1
    def back(self):
        m.s = selection()
        self.destroy()
    def destroy(self):
        self.win.master.destroy()

class higher_lower():
    def __init__(self):
        self.win = window(250, 250)
        self.button1 = self.win.button(self.win.master, 0, 0, 125, 50, "red", "white", "Quit", [self.destroy], [[]])
        self.button2 = self.win.button(self.win.master, 125, 0, 125, 50, "black", "white", "Back", [self.back], [[]])
        self.button3 = self.win.button(self.win.master, 0, 50, 250, 50, "black", "white", "Start", [self.start], [[]])
        self.button4 = self.win.button(self.win.master, 0, 100, 125, 50, "black", "white", "Higher", [self.check], [[True]])
        self.button5 = self.win.button(self.win.master, 125, 100, 125, 50, "black", "white", "Lower", [self.check], [[False]])
        self.label1 = self.win.label(self.win.master, 0, 150, 250, 25, "Calibri", "black", "white", "1. Number: ")
        self.label2 = self.win.label(self.win.master, 0, 175, 250, 25, "Calibri", "black", "white", "2. Number: ")
        self.label3 = self.win.label(self.win.master, 0, 200, 250, 25, "Calbri", "black", "white", "")
        self.label4 = self.win.label(self.win.master, 0, 225, 250, 25, "Calbri", "black", "white", "Money: " + str(m.get_kontostand()))
        self.win.buttons[3]["state"] = "disabled"
        self.win.buttons[4]["state"] = "disabled"
        self.zahl1 = 0
        self.zahl2 = 0
    def start(self):
        if m.get_kontostand() < 25:
            self.win.labels[3].config(text="No Money!!!", fg="red")
            return
        self.zahl1 = random.randint(1,100)
        self.zahl2 = random.randint(1,100)
        self.win.labels[0].config(text="1. Number: "+ str(self.zahl1))
        self.win.labels[1].config(text="2. Number: ")
        self.win.labels[2].config(text="", fg="white")
        self.win.buttons[2]["state"] = "disabled"
        self.win.buttons[3]["state"] = "active"
        self.win.buttons[4]["state"] = "active"
    def check(self, hl):
        self.win.labels[1].config(text="1. Number: "+ str(self.zahl2))
        if (hl) and (self.zahl2 > self.zahl1):
            self.win.labels[2].config(text="Win!", fg="green")
            m.write_file(random.randint(10,20), True)
        elif (not hl) and (self.zahl2 < self.zahl1):
            self.win.labels[2].config(text="Win!", fg="green")
            m.write_file(random.randint(10,20), True)
        elif self.zahl1 == self.zahl2:
            self.win.labels[2].config(text="Tie!", fg="yellow")
        else:
            self.win.labels[2].config(text="Fail!", fg="red")
            m.write_file(25, False)
        self.win.buttons[2]["state"] = "active"
        self.win.buttons[3]["state"] = "disabled"
        self.win.buttons[4]["state"] = "disabled"    
        self.win.labels[3].config(text="Money: " + str(m.get_kontostand()))
    def back(self):
        m.s = selection()
        self.destroy()
    def destroy(self):
        self.win.master.destroy()
    
class chase_the_button():
    def __init__(self):
        self.win = window(300, 300)
        self.button1 = self.win.button(self.win.master, 0, 0, 50, 50, "red", "white", "Back", [self.destroy], [[]])
        self.button2 = self.win.button(self.win.master, 100, 100, 50,50, "black", "white", "Click Me!", [self.click], [[]])
    def click(self):
        x1 = random.randint(50,250)
        y1 = random.randint(50,250)
        self.win.buttons[1].place(x=x1, y=y1)
        m.write_file(2, True)
    def destroy(self):
        m.s = selection()
        self.win.master.destroy()
        
m = Main()
m.win.master.mainloop()
"""
while True:
    if m.running:
        m.win.master.update()
        m.win.master.update_idletasks()
    elif m.s != None:
        m.s.win.master.update()
        m.s.win.master.update_idletasks()
    elif m.s == None:
        print()
    time.sleep(0.04)
    """


