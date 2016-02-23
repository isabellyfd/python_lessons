# 23/02/2016 lesson

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

pergunta6 = '''Qual foi a maior derrota da seleção brasileira na ultima copa?
a - 7X1
b - 3X0
c - 4X2'''
resposta_pergunta6 = "a"

point = 0

#Mostrando as perguntas
print( p1 )
tentativa1 = input()
if respostaP1 == tentativa1:
    point += 1
else:
    if point != 0:
        point -= 1
        print("HAHAHAHA nooby, se fudeu- GTASTYLE")

print( p2 )
tentativa2 = input()
if respostaP2 == tentativa2:
    point += 1
else:
    if point != 0:
        point -= 1
        print("HAHAHAHA nooby, se fudeu- GTASTYLE")

print( p3 )
tentativa3 = input()
if respostaP3 == tentativa3:
    point += 1
else:
    if point != 0:
        point -= 1
        print("HAHAHAHA nooby, se fudeu- GTASTYLE")

    
print( pergunta4 )
tentativa4 = input()
if resposta_pergunta4 == tentativa4:
    point += 1
else:
    if point != 0:
        point -= 1
        print("HAHAHAHA nooby, se fudeu- GTASTYLE")
    
print( pergunta5 )
tentativa5 = input()
if resposta_pergunta5 == tentativa5:
    point += 1
else:
    if point != 0:
        point -= 1
        print("HAHAHAHA nooby, se fudeu- GTASTYLE")

print ( pergunta6 )
tentativa6 = input()
if resposta_pergunta6 == tentativa6:
    point += 1
else:
    if point != 0:
        point -= 1
        print("HAHAHAHA nooby, se fudeu- GTASTYLE")


if point >= 5:
    print("Acabou e vc... Arrasou Viado    \o/")
else:
    print("Acabou e vc é... nooooooooby")
