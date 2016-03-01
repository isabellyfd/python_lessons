#import pdb

#pdb.set_trace()
number = int(input("Digite um numero para ver se ele tem raiz cubica exata:"))
fixo = number
count = 1
neg_count = -1
flag_count = False
flag_negcount = False
while(number > 0 and (not flag_count) and (not flag_negcount)):
    if (count * count * count == fixo):
        flag_count = True
    elif (neg_count * neg_count * neg_count == fixo):
        flag_negcount = True
    count += 1
    neg_count -= 1
    number -= 1

if flag_count:
    print("Existe raiz cubica exata positiva", count-1)
elif flag_negcount:
    print("Existe raiz cubica exata negativa",  neg_count+1)
else:
    print ("No ecsisten")    
