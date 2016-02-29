errors = 6
print("Digite um uma palavra para seu amigo adivinhar:")
word = input()
done = False
result = "_" *len(word)
print("\n"*100)
while not done:
     
    print(result)
    if result != word:
        
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
            
        if errors == 0:
            done = True
            
    else:
        done = True
