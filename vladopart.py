import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import *

root = Tk()


def mainfunction():
    imagelist = ["7-2-bear-png-3_gif_png_gif.gif", "Bear-PNG-5.gif"]
    imagelist2 = ["7-2-bear-png-3_gif_png_gif.gif", "Bear-PNG-5.gif"]

    photo = PhotoImage(file=imagelist[0])
    width = 900
    height = 900
    canvas = Canvas(width=width, height=height)
    canvas.pack()
    widthrect = 200
    widthrect2=600
    number = 100
    number2=number
    moveimg = -40
    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=imagefile)
        giflist.append(photo)

    giflist2 = []
    for imagefile2 in imagelist2:
        photo = PhotoImage(file=imagefile2)
        giflist2.append(photo)

    for k in range(1000):
        for gif in giflist:
            canvas.delete(ALL)
            x = canvas.create_rectangle(0, 65, widthrect+100, 25, fill="red")
            y = canvas.create_rectangle(900, 65, widthrect2, 25, fill="red")
            canvas.create_text(880, 50, fill="orange", font="Times 20 italic bold",
                               text=str(number2))
            canvas.create_text(20, 50, fill="orange", font="Times 20 italic bold",
                               text=str(number))
            canvas.create_image((width / 6.0) * 5, height / 2.0, image=giflist2[0])
            canvas.create_image(width / 6.0 + moveimg+20, height / 2.0, image=gif)
            root.after(40)
            widthrect2+=4
            number2 -= 2
            moveimg *= -1
           # if number2==0:
               # canvas.create_text(20, 50, fill="orange", font="Times 20 italic bold",
                                 #  text="Bear loses")
            canvas.update()
            time.sleep(1)
        for gif2 in giflist2:
            canvas.delete(ALL)
            x = canvas.create_rectangle(0, 65, widthrect+100, 25, fill="red")
            y = canvas.create_rectangle(900, 65, widthrect2, 25, fill="red")
            canvas.create_text(20, 50, fill="orange", font="Times 20 italic bold",
                               text=str(number))
            canvas.create_text(880, 50, fill="orange", font="Times 20 italic bold",
                               text=str(number2))
            canvas.create_image(width / 6.0 , height / 2.0, image=giflist[0])
            canvas.create_image((width/6.0)*5 - moveimg, height / 2.0, image=gif2)
            root.after(40)
            widthrect -= 4
            number -= 50
            moveimg *= -1
           # if number==0:
                #canvas.create_text(20, 50, fill="orange", font="Times 20 italic bold",
                               #    text="Bear loses")
            canvas.update()
            time.sleep(1)

    root.mainloop()

mainfunction()

