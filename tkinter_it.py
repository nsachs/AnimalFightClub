from tkinter import *
from tkinter import font

class Animals():
    def __init__(self,master):

        #Title
        self.title_font = font.Font(family="Courier New", size=30, weight = font.NORMAL, underline = 2)
        self.title = Label(master, text = "Animal Fight Club!", font = self.title_font, bg = "lightgreen", fg = "darkgreen")
        self.title.grid(row=1, column=1, columnspan=5)

        #Animal Display
        self.animal1_font = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.animal1 = Label(master, text = "First Animal", fg = "darkgreen")
        self.animal1.grid(row = 4, column = 1, columnspan = 2)

        self.animal2_font = font.Font(family = "Courier New", size = 15, weight = font.NORMAL)
        self.animal2 = Label(master, text = "Second Animal", fg = "darkgreen")
        self.animal2.grid(row = 4, column = 3, columnspan = 2)

        #Add animations

        #Question
        self.guess = Label(master, text = "Who will come out on top?")
        self.guess.grid(row = 5, column = 1, columnspan = 2)

        #User predicts a winner
        '''
        self.winner1_button = Button(self, text = "animal1_name")
        self.winner1_button.grid(row = 5, column = 2)

        self.winner2_button = Button(self, text = "animal2_name")
        self.winner2_button.grid(row = 5, column = 3)
        '''
        #Fight button

        #List of winner and stats
        self.victor = Label(master, text = "Gorilla Wins!  " + "Gorillas are superior in strength, etc")
        self.victor.grid(row = 6, column = 1, columnspan = 3)


    #def fight_button_click(self):


if __name__ == "__main__":
    root = Tk()
    root.title("Animal Fight Club App")
    my_app = Animals(root)
    root.mainloop()
