from tkinter import *
from tkinter import font
import csv

import random
from fighting import *

class Animals():
    def __init__(self,master):
        self.animal_list = animal_list


        self.animal1Name = StringVar()
        self.animal2Name = StringVar()
        self.choose_animals()
        #Title
        self.title_font = font.Font(family="Courier New", size=30, weight = font.BOLD, underline = 2)
        self.title = Label(master, text = "Animal Fight Club!", font = self.title_font, bg = "lightgreen", fg = "darkgreen")
        self.title.grid(row=1, column=1, columnspan=10)

        '''
        Add animations
        self.animation1 = PhotoImage(file = "giphy.gif")
        self.animation1.grid(row = 2, column = 1, columnspan = 2)
        self.animation2 = PhotoImage(file = "giphy-1.gif")
        self.animation2.grid(row = 2, column =2, columnspan = 2)
        '''


        #Animal Display
        self.animal1_font = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.animal1_label = Label(master, textvariable = self.animal1Name, fg = "darkgreen")
        self.animal1_label.grid(row = 5, column = 1, columnspan = 2)

        self.animal2_font = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.animal2_label = Label(master, textvariable = self.animal2Name, fg = "darkgreen")
        self.animal2_label.grid(row = 5, column = 3, columnspan = 2)


        #Question
        self.guess = Label(master, text = "Who will come out on top?")
        self.guess.grid(row = 6, column = 1, columnspan = 2)
        v = StringVar()

        #User predicts a winner/send prediction back
        self.winner1_button = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.winner1_button = Button(master, textvariable = self.animal1Name)
        self.winner1_button.grid(row = 6, column = 3)
        self.winner2_button = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.winner2_button = Button(master, textvariable = self.animal2Name)
        self.winner2_button.grid(row = 6, column = 4)
        if self.winner1_button == True:
            user_winner = self.animal_1[0]
        elif self.winner2_button == True:
            user_winner = self.animal_2[0]

        #Fight button/send fight
        self.fight_button = font.Font(family = "Courier New", size = 15, weight = font.BOLD)
        self.fight_button = Button(master, text = "FIGHT!", fg = "purple", command = lambda:self.fighting(self.animal_list[self.animal_list.index(self.animal1)][1], self.animal_list[self.animal_list.index(self.animal2)][1]))
        self.fight_button.grid(row = 7, column = 3, columnspan = 2)

        '''
        if animal_1[1] > animal_2[1]:
            winner = animal_1[0]
        else:
            winner = animal_2[0]
            
        '''
        self.winner_text = StringVar()
        self.winner_text.set("")

        #List of winner and stats/ grab stats and winner
        self.victor = Label(master, textvariable = self.winner_text)
        self.victor.grid(row = 8, column = 1, columnspan = 3)
        #Play again button
        self.restart_button = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.restart_button = Button(master, text = "Play Again", command=lambda:self.choose_animals())
        self.restart_button.grid(row = 8, column = 4)

    def fighting(self,animal1, animal2):
        self.winner_text.set("You are correct!  " + take_turn(animal1, animal2).name + " Wins!")
        print(self.winner_text)
    def choose_animals(self):
        self.animal_1 = random.randrange(len(self.animal_list))
        self.animal1 = self.animal_list[self.animal_1]
        # del(animal_list[animal_1])
        self.animal_2 = random.randrange(len(self.animal_list))
        self.animal2 = self.animal_list[self.animal_2]
        self.animal1Name.set(self.animal1[0])

        self.animal2Name.set(self.animal2[0])

if __name__ == "__main__":
    root = Tk()
    root.title("Animal Fight Club App")
    my_app = Animals(root)
    root.mainloop()
