# joguinho 2
# 23/02/2016 lesson
# modificar pra printar to ruge and too small encadeado
print ("Hello Players, Lat's play de dumb game!!!")
print ("Palyer 1: Please put 2 numbers!!")
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))

spaces = "\n"* 100

isMajor = "Ruge than"
isMinor = "Small than"
middleman = "its in the middle, man"
countDown = 3
flag1 = False
flag2 = False
print(spaces)
print("Now, Player 2, you have", countDown, "guesses, guess a number")
guess = int(input())

if guess == number1:
    flag1 = True
elif guess == number2:
    flag2 = True
elif (guess > number1 and guess < number2) or (guess > number2 and guess < number1):
    print(middleman)
elif guess < number1:
    print(isMinor, "number 1")
elif guess < number2:
    print (isMinor, "number 2")
elif guess > number1:
    print(isMajor, "number 1")
elif guess > number2:
    print (isMajor, "number 2")
countDown -= 1


done = flag1 and flag2
if not done:
    print ("Now, you have", countDown, "guesses, guess a number")
    guess = int(input())
    if guess == number1:
        flag1 = True
    elif guess == number2:
        flag2 = True
    elif (guess > number1 and guess < number2) or (guess > number2 and guess < number1):
        print(middleman)
    elif guess < number1:
        print(isMinor, "number 1")
    elif guess < number2:
        print (isMinor, "number 2")
    elif guess > number1:
        print(isMajor, "number 1")
    elif guess > number2:
        print (isMajor, "number 2")
    countDown -= 1
    done = flag1 and flag2
    if not done:
        print ("Now you have", countDown, "guess, last chance to win, guess a fucking number!!!!")
        guess = int(input())
        if guess == number1:
            flag1 = True
        elif guess == number2:
            flag2 = True
        elif (guess > number1 and guess < number2) or (guess > number2 and guess < number1):
            print(middleman)
        elif guess < number1:
            print(isMinor, "number 1")
        elif guess < number2:
            print (isMinor, "number 2")
        elif guess > number1:
            print(isMajor, "number 1")
        elif guess > number2:
            print (isMajor, "number 2")
        countDown -= 1

if not done:
    print("man u lost!")
else:
    print("Congrats u won!")
