#!/usr/bin/python

from tkinter import *

root = Tk()
topFrame = Frame(root, bg="white")
topFrame.pack()
nameGame = Label(topFrame, text="Haging Man", bg="white")
nameGame.pack()

palavraLabel =  Label(topFrame, text="Digite aqui a palavra do jogo:", bg="white")
palavraLabel.pack()

submitPalavra  = Button(topFrame, text="Submit", fg="white", bg="black")
submitPalavra.pack(side=RIGHT)

bottomFrame = Frame(root, bg ="white")
bottomFrame.pack(side=BOTTOM)
root.mainloop()

