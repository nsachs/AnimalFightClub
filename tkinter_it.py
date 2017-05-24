from tkinter import *
from tkinter import font

class Animals():
    def __init__(self,master):

        #Title
        self.title_font = font.Font(family="Courier New", size=30, weight = font.BOLD, underline = 2)
        self.title = Label(master, text = "Animal Fight Club!", font = self.title_font, bg = "lightgreen", fg = "darkgreen")
        self.title.grid(row=1, column=1, columnspan=10)

        '''
        # Add animations
        self.animation1 = PhotoImage(file = "giphy.gif")
        self.animation1.grid(row = 2, column = 1, columnspan = 2)
        self.animation2 = PhotoImage(file = "giphy-1.gif")
        self.animation2.grid(row = 2, column =2, columnspan = 2)
        '''

        #Animal Display
        self.animal1_font = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.animal1 = Label(master, text = "First Animal", fg = "darkgreen")
        self.animal1.grid(row = 5, column = 1, columnspan = 2)

        self.animal2_font = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.animal2 = Label(master, text = "Second Animal", fg = "darkgreen")
        self.animal2.grid(row = 5, column = 3, columnspan = 2)


        #Question
        self.guess = Label(master, text = "Who will come out on top?")
        self.guess.grid(row = 6, column = 1, columnspan = 2)

        #User predicts a winner
        self.winner1_button = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.winner1_button = Button(master, text = "animal1_name")
        self.winner1_button.grid(row = 6, column = 3)
        self.winner2_button = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.winner2_button = Button(master, text = "animal2_name")
        self.winner2_button.grid(row = 6, column = 4)

        #Fight button
        self.fight_button = font.Font(family = "Courier New", size = 15, weight = font.BOLD)
        self.fight_button = Button(master, text = "FIGHT!", fg = "purple")
        self.fight_button.grid(row = 7, column = 3, columnspan = 2)

        #List of winner and stats
        self.victor = Label(master, text = "Gorilla Wins!  " + "Gorillas are superior in strength, etc")
        self.victor.grid(row = 8, column = 1, columnspan = 3)

        #Play again button
        self.restart_button = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.restart_button = Button(master, text = "Play Again")
        self.restart_button.grid(row = 8, column = 4)

    #def animal_choice_click(self):

    #def fight_button_click(self):


if __name__ == "__main__":
    root = Tk()
    root.title("Animal Fight Club App")
    my_app = Animals(root)
    root.mainloop()
