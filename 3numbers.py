number1 = int(input("Primeiro numero:\n"))
number2 = int(input("Segundo numero:\n"))
number3 = int(input("Terceiro numero:\n"))

menor = 0
med = 0
maior = 0

if number1 != number2 and number2 != number3:
    if number1 < number2 and number1 < number3:
        menor = number1
    elif number2 < number1 and number2 < number3:
        menor = number2
    else:
        menor = number3

    if number1 > number2 and number1 > number3:
        maior = number1
    elif number2 > number1 and number2 > number3:
        maior = number2
    else:
        maior = number3

    if number1 != maior and number1 != menor:
        med = number1
    elif number2 != maior and number2 != menor:
        med = number2
    elif number3 != maior and number3 != menor:
        med = number3
else:
    menor = med = maior = number1

print (menor, med, maior)
