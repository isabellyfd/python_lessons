
def isPrime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        n = 2
        while n < num:
            if num%n == 0:
                return False
            n += 1
        return True
        
    
var = int(input("Digite um numero para saber que ele eh primo:"))

if isPrime(var):
    print(str(var)+" eh primo")
else:
    print(str(var)+" nao eh primo")

    
