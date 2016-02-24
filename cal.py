
count = 0
memoria = 0
M = False
while count < 3:
    operador = input("digite o operador (+, -, *, /, M ) :\n")
    if operador == "+":
        if M:
            string = input("num1 ou m:\n")
            if string == "m" or string == "M":
                number1 = memoria
            else:
                number1 = int(string)
        else:
            number1 = int(input("num1:\n"))
        number2 = int(input("num2:\n"))
        memoria = number1 + number2
        print (memoria)
    elif operador == "-":
        if M:
            string = input("num1 ou m:\n")
            if string == "m" or string == "M":
                number1 = memoria
            else:
                number1 = int(string)
        else:
            number1 = int(input("num1:\n"))
        number2 = int(input("num2:\n"))
        memoria = number1 - number2
        print (memoria)
    elif operador == "*":
        if M:
            string = input("num1 ou m:\n")
            if string == "m" or string == "M":
                number1 = memoria
            else:
                number1 = int(string)
        else:
            number1 = int(input("num1:\n"))
        number2 = int(input("num2:\n"))
        memoria = number1 * number2
        print (memoria)
    elif operador == "/":
        if M:
            string = input("num1 ou m:\n")
            if string == "m" or string == "M":
                number1 = memoria
            else:
                number1 = int(string)
        else:
            number1 = int(input("num1:\n"))
        number2 = int(input("num2:\n"))
        if number2 != 0:
            memoria = number1 / number2
            print (memoria)
        else:
            print ("Não pode dividir por zero, honey!")
    elif operador == "M":
        M = True
    else:
        print ("Oloooooco, cê botou algo errado!")
    count += 1
