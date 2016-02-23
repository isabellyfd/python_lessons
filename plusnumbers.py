number = int(input("input a number:\n"))

if number >= 100 and number <= 999:
    number = str(number)
    result = int(number[0]) + int(number[1]) + int(number[2])
    print (result)
