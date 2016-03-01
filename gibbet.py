errors = 6
missed = []
print("Digite um uma palavra para seu amigo adivinhar:")
word = input()
done = False
result = "_" *len(word)
print("\n"*100)
while not done:
     
    
    if result != word:
        if missed != []:
            print ("voce já tentou as letras", missed)
            print("-"*10)
        
        print(result)
        print("Voce pode errar até", errors, "vezes, digite uma letra:\n") 
        letter =  input()
        
        while 1 < len(letter):
            print("Digite 'uma' letra:\n")
            letter =  input()
            
        count = 0
        point = False
            
        #print (count < len(word))
        while count < len(word):
            if word[count] == letter[0]:
                #print (str(count), word[count])
                iterar = 0
                string =  ""
                while iterar < len(result):
                    if result[iterar] == "_" and iterar == count:
                        string = string + letter[0]
                        point = True   
                    else:
                        string =  string + result[iterar]
                    iterar += 1
                result = string
            count += 1
            
        if not point:
            errors -= 1
            missed.append(letter)
        if errors == 0:
            done = True
            
    else:
        done = True
        
if done:
    print("Muito bem, carinha!!")
    print("A palavra era", word)
else:
    print("A palavra era", word)
    print("Sorry!!")
