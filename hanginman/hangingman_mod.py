#!/usr/bin/python

from tkinter import *
import time

import tkinter.messagebox
class Application():

    def __init__(self, root):
        self.root = root
        self.root.title("Game - Hangin' man")
        #frame superior
        self.topFrame = Frame(root,width=600, height=400, bg="white")
        self.topFrame.pack()
        #inificalizando widgets
        self.nameGame = Label(root, text="Hangin Man", font="Bodini 24", bg="white")
        self.nameGame.place(x=200, y=10)
        #frame inferior
        self.bottomFrame = Frame (root, width=600, height=200)
        self.bottomFrame.pack()
        #inicializando widgets
        self.labelPalavra = Label(self.bottomFrame, text="Digite aqui a palavra do jogo:", font="Bodoni 16")
        self.varPalavra = StringVar()
        self.entryPalavra = Entry(self.bottomFrame, textvariable=self.varPalavra)
        self.buttonPalavra = Button(self.bottomFrame, text="Submit", fg="white", bg="black", font="Bodini", command=self.cadastrar)
       
        self.varLetra = StringVar() 
        self.labelTentativa = Label(self.bottomFrame, text="Tente uma letra:", font="Bodoni 16")
        self.entryTentativa = Entry(self.bottomFrame, textvariable=self.varLetra)
        self.buttonTentativa = Button(self.bottomFrame, text="Submit", fg="white", bg="black", font="Bodini", command=self.tentar)
        
        self.labelPalavra.grid(row=0, sticky=E)
        self.entryPalavra.grid(row=0, column=1)
        self.buttonPalavra.grid (row =0, column=2)
        
        self.labelTentativa.grid(row=1, sticky=E)
        self.entryTentativa.grid(row=1, column=1)
        self.buttonTentativa.grid(row=1, column=2)
        self.palavra = ""
        self.tentativa = ""
        self.string = ""
        self.errors = 6
        self.tentativasErradas = []
        self.tentativas = []
        self.photo = PhotoImage(file="img/img"+str(self.errors)+".gif")
        self.labelPhoto = Label (self.topFrame, image= self.photo)
        self.labelPhoto.pack()

    def cadastrar(self):
        self.palavra = self.varPalavra.get().lower()
        self.varPalavra.set("")
        self.string = " ".join(["_"]*len(self.palavra))
        self.show()
     
    def show(self):
        self.mostrar = Label(self.root, text=self.string, font="Bodini 24", justify=CENTER)
        self.mostrar.pack()
        
    def tentar(self):
        
        self.tentativa = self.varLetra.get().lower()
        self.varLetra.set("")
        print(self.tentativas)
        if self.tentativa in self.tentativas:
            tkinter.messagebox.showinfo('ErOOOOU', 'Voce ja tentou essa letra')
            self.tentativa = self.varLetra.get()
            self.varLetra.set("")
        else:
            if(not self.tentativa.isalpha()) or (len(self.tentativa) > 1):
                tkinter.messagebox.showinfo('ErOOOOU','Digite apenas uma letra')
                self.tentativa =  self.varLetra.get()
                self.varLetra.set("")
            else:
                self.tentativas.append(self.tentativa)
                self.testar()      
    
    def testar(self):
        count = 0
        posicoes = []
        #pega todos os incides que tem a tentativa na palavra 
        while count < len(self.palavra):
            if self.tentativa == self.palavra[count]:
                posicoes.append(count)
            count += 1
        
        count = 0
        #print (posicoes)
        if len(posicoes) > 0:
            self.string = self.string.split()
            for pos in posicoes:
                self.string[pos] = self.tentativa.upper()
            print(''.join(self.string))
            if "".join(self.string).lower() == self.palavra:
                self.string = " ".join(self.string)
                self.mostrar['text'] = self.string
                tkinter.messagebox.showinfo('Parabeins', 'Bicha, a senhora eh destruidora meshmo' )
                time.sleep(3)
                self.string = ""
                self.mostrar['text'] = self.string
            else:
                self.string = " ".join(self.string)
                self.mostrar['text'] = self.string
                    
        else:
            #print('hiiiii')
            self.errors -= 1
            self.tentativasErradas.append(self.tentativa)
            self.photo['file'] = "img/img"+str(self.errors)+".gif"
            
            if self.errors == 0:
                tkinter.messagebox.showinfo('Eira', 'Suas chances abaram!!! A palavra era:' +str(self.palavra))
                self.string = ""
                self.mostrar['text'] = self.string
            else:
                tkinter.messagebox.showinfo('ErOOOOU','Mano, vc digitou um letra cabrosa, agora vc tem '+str(self.errors)+" chances")
                tkinter.messagebox.showinfo('Aviso', 'Voce ja tentou e errou essas letras: '+ ' '.join(self.tentativasErradas))
        #self.show()
   
root = Tk()
app = Application(root)
root.mainloop()
