# joguinho 2
# 23/02/2016 lesson
# modificar pra printar to ruge and too small encadeado
print ("Hello Players, Lat's play de dumb game!!!")
print ("Palyer 1: Please put 2 numbers!!")
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
 
spaces = "\n"* 100
 
isMajor = "Ruge than the major number"
isMinor = "Small than the minor number"
iddleman = "its in the middle, man"

countDown = 3
flag1 = False
flag2 = False

print(spaces)

acertou = 0
maior = 0
menor = 0
if number1 > number2:
    maior = number1
    menor = number2
else:
    maior = number2
    menor = number1
    
minrange = 10
maxrange = 25
while countDown > 0:
    done = flag1 and flag2
    if not done:
        print("Now, Player 2, you have", countDown, "guesses, guess a number")
        guess = int(input())
        
        while guess > 100 or guess < 0:
            print ("Please, enter a number between 0 and 100, inclusive")
            guess = int(input())
            
        if acertou == guess:
            print("You guessed already!") 
        elif (guess < (menor-maxrange)):
            countDown = 0
        elif (guess > (maior+maxrange)):
            countDown = 0
        elif (guess < (menor-minrange)):
            print ("maaaan c'mon, u noooooooby")
        elif (guess > (maior+minrange)):
            print ("maaaan c'mon, u noooooooby")
        elif guess == menor and guess == maior:
            flag1 = True
            flag2 = True 
            countDown = 0
        elif guess < menor:
            print (isMinor)
        elif guess > maior:
            print (isMajor)
        elif menor < guess < maior:
            print (middleman)
        elif guess == menor:
	        acertou = guess
            flag1 = True
        elif guess == maior:
            flag2 = True
            acertou = guess
              
        countDown -= 1
    else:
        countDown = 0

done = flag1 and flag2
        
if not done:
    print("man u lost!")
else:
    print("You won!!!")
