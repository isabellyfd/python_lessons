number = int(input("Input a number:\n"))
done = False

if number < 100 and number > 999:
    print ("Error")
    done = True
    
if not done:
    if (number % 3) == 0:
        print ("Div")
    else:
        print("Nooooo")
        
