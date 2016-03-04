#!/usr/bin/python

from tkinter import *
palavra = ""

def submitPalavra():
    print ("Você clicou no botão de palavra")
    palavra = varPalavra.get()
    varPalavra.set("")
    
def submitLetra(event):
    print ("Você clicou no botão de letra")
    
    

root = Tk()
root.title("Game - Hangin man")
topFrame = Frame(root, bg="white", width=300, height=400)
topFrame.pack()

nameGame = Label(topFrame, text="Haging Man", font="Bodoni 24")
nameGame.pack(fill=BOTH)

bottomFrame = Frame(root, width=300, height=400)

palavraLabel =  Label(bottomFrame, text="Digite aqui a palavra do jogo:", font="Bodoni 16")
varPalavra = StringVar()
entryPalavra = Entry(bottomFrame, textvariable=varPalavra)
submitB1  = Button(bottomFrame, text="Submit", fg="white", bg="black", font="Bodoni", command=submitPalavra)

tentativaLabel = Label(bottomFrame, text="Tente uma letra:", font="Bodoni 16")
entryLetra = Entry(bottomFrame)
submitB2 = Button(bottomFrame, text="Submit", fg="white", bg="black", font="Bodoni")

bottomFrame.pack(side=BOTTOM)
palavraLabel.grid(row=0, sticky=E)
entryPalavra.grid(row=0, column=1)
submitB1.grid(row=0, column=3)
#submitB1.bind("<Button-1>", submitPalavra)
tentativaLabel.grid(row=1, sticky=E)
entryLetra.grid(row=1, column=1)
submitB2.grid(row=1, column=3)
submitB2.bind("<Button-1>", submitLetra)

root.mainloop()



