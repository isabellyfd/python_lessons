#!/usr/bin/python

from tkinter import *
def submitPalavra(event):
    print ("Você clicou no botão de palavra")
    
def submitLetra(event):
    print ("Você clicou no botão de letra")
    

root = Tk()
topFrame = Frame(root, bg="white")
topFrame.pack(fill=BOTH)

nameGame = Label(topFrame, text="Haging Man")
nameGame.pack(fill=BOTH)

bottomFrame = Frame(root)

palavraLabel =  Label(bottomFrame, text="Digite aqui a palavra do jogo:")
entryPalavra = Entry(bottomFrame)
submitB1  = Button(bottomFrame, text="Submit", fg="white", bg="black")

tentativaLabel = Label(bottomFrame, text="Tente uma letra:")
entryLetra = Entry(bottomFrame)
submitB2 = Button(bottomFrame, text="Submit", fg="white", bg="black")

bottomFrame.pack(side=BOTTOM, fill=BOTH)
palavraLabel.grid(row=0, sticky=E)
entryPalavra.grid(row=0, column=1)
submitB1.grid(row=0, column=3)
submitB1.bind("<Button-1>", submitPalavra)
tentativaLabel.grid(row=1, sticky=E)
entryLetra.grid(row=1, column=1)
submitB2.grid(row=1, column=3)
submitB2.bind("<Button-1>", submitLetra)


root.mainloop()

