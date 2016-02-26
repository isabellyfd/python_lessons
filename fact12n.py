varnum = int(input("Digite um numero:\n"))

fact = []

count = 0

while count < varnum:
    
    resultado = 1
    n = count + 1
    while 1 < n:
        resultado = resultado * n
        n -= 1
            
    fact.append(resultado)
    count  += 1
    
end  = fact.pop()
string  = ""
for num in fact:
    string = string  + str(num)  + ", "
print (string + str(end))
