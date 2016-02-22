# 22/02/2016 lesson

p1 = "Qual a capital da Croacia?"
respostaP1 = "Zagreb"

p2 = "Em que ano Python 1.0 tornou-se disponivel?"
respostaP2 = "1994"

p3 = "Qual o nome do segundo album do Vampire Weekend?"
respostaP3 = "Contra"

pergunta4 = "Qual o nome do 'pai' da computação?"
resposta_pergunta4 = "Alan Turin"

pergunta5 = "Qual a ultima horcrux a ser descoberta em Harry Potter?"
resposta_pergunta5 = "Ele mesmo"

point = 0

#Mostrando as perguntas
print( p1 )
tentativa1 = input()
if respostaP1 == tentativa1:
    point += 1
    #print("Arrasou Viado")
#else:
    #print("HAHAHAHA nooby, se fudeu- GTASTYLE")

print( p2 )
tentativa2 = input()
if respostaP2 == tentativa2:
    point += 1
    #print("Arrasou Viado")
#else:
    #print("HAHAHAHA nooby, se fudeu- GTASTYLE")

print( p3 )
tentativa3 = input()
if respostaP3 == tentativa3:
    point += 1
    #print("Arrasou Viado")
#else:
    #print("HAHAHAHA nooby, se fudeu- GTASTYLE")

    
print( pergunta4 )
tentativa4 = input()
if resposta_pergunta4 == tentativa4:
    point += 1
    #print("Arrasou Viado")
#else:
    #print("HAHAHAHA nooby, se fudeu- GTASTYLE")
    
print( pergunta5 )
tentativa5 = input()
if resposta_pergunta5 == tentativa5:
    point += 1
    #print("Arrasou Viado")
#else:
    #print("HAHAHAHA nooby, se fudeu- GTASTYLE")


if point > 2:
    print("Arrasou Viado    \o/")
else:
    print("nooooooooby")
