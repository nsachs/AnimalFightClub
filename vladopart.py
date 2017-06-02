import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import *

root = Tk()


def mainfunction():
    imagelist = ["7-2-bear-png-3_gif_png_gif.gif", "Bear-PNG-5.gif"]

    photo = PhotoImage(file=imagelist[0])
    width = 900
    height = 900
    canvas = Canvas(width=width, height=height)
    canvas.pack()
    widthrect = 200
    number = 100
    moveimg = -40
    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=imagefile)
        giflist.append(photo)

    for k in range(1000):
        for gif in giflist:
            canvas.delete(ALL)
            x = canvas.create_rectangle(0, 65, widthrect, 25, fill="red")
            canvas.create_text(20, 50, fill="orange", font="Times 20 italic bold",
                               text=str(number))
            canvas.create_image(width / 6.0 + moveimg, height / 2.0, image=gif)
            canvas.move(x, 6, 0)
            root.after(40)
            widthrect -= 4
            number -= 2
            moveimg *= -1
            canvas.update()
            time.sleep(0.7)

    root.mainloop()
