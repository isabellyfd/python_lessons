#!/usr/bin/python

from tkinter import *
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
        
    def cadastrar(self):
        self.palavra = self.varPalavra.get()
        self.varPalavra.set("")
        self.string = " ".join(["_"]*len(self.palavra))
        self.show()
     
    def show(self):
        self.mostrar = Label(self.root, text=self.string, font="Bodini 24", justify=CENTER)
        self.mostrar.pack()
        
    def tentar(self):
        self.tentativa = self.varLetra.get()
        self.varLetra.set("")
 
        if(not self.tentativa.isalpha()) or (len(self.tentativa) > 1):
            tkinter.messagebox.showinfo('ErOOOOU','Digite apenas uma letra')
            self.tentativa =  self.varLetra.get()
            self.varLetra.set("")
        else:
            self.testar()      
    
    def testar(self):
        count = 0
        done = False
        '''while(count < len(self.palavra)):
            if self.palavra[count] == self.tentativa:
                iterar = 0
                string  = ""
                
                while(iterar < len(self.string)):
                    if self.string[iterar] != " ":
                        if iterar==2*count: 
                            string = string + self.tentativa
                        else:
                            string = string + self.string[iterar]
                    else:
                        string = string + self.string[iterar]
                    iterar += 1
                self.string = string
                count +=1        
        '''
        self.show()
   
root = Tk()
app = Application(root)
root.mainloop()
