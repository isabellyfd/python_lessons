
num = int(input("Digite um numero:\n"))

count = 2

primes = []
if num != 1:
    while count <= num:
        if count == 2:
            primes.append(count)
        else:
            a = 2 
            isprime = True
            while(a < count):
                if count%a == 0:
                    isprime = False
                a += 1
            
            if isprime:
                primes.append(count)
        count += 1
    
end = ""
if primes != []:
    end  = primes.pop()
string  = ""
for nume in primes:
    string = string  + str(nume)  + ", "
print (string + str(end))


