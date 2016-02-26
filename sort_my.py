lista = []

inp = input("Digite numeros a serem ordenados")

while inp != "":
    if inp.isnumeric():
        lista.append(int(inp))
    inp = input()

lista.sort()

string = ""
for num in lista:
    string = string + str(num) + " "

print (string)
