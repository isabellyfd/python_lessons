
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


num =  int(input("Digite um numero:\n"))

if not isPrime(num):
    div = 2
    while num%div == 0 and div < num:
        print(div)
        div += 1
else:
    print("Esse numero é primo")
