dia = 1
mes = 1

while mes <= 12:
    if mes <= 6:
        if mes == 2:
            while dia <= 29:
                if len(str(dia)) == 1:
                    print("0"+str(dia)+"/0"+str(mes))
                else:
                    print(str(dia)+"/0"+str(mes))
                dia += 1
            dia = 1
        if mes%2 == 0:
            while dia <= 30:
                if len(str(dia)) == 1:
                    print("0"+str(dia)+"/0"+str(mes))
                else:
                    print(str(dia)+":0"+str(mes))
                dia += 1
            dia = 1
        else:
            while dia <= 31:
                if len(str(dia)) == 1:
                    print ("0"+str(dia)+"/0"+str(mes))
                else:
                    print(str(dia)+"/0"+str(mes))
                dia += 1
            dia = 1
    else:
        if mes%2 == 0:
            while dia <= 31:
                if len(str(dia)) == 1 and len(str(mes)) == 1:
                    print ("0"+str(dia)+"/0"+str(mes))
                elif len(str(dia)) > 1  and len(str(mes)) == 1:
                    print(str(dia)+"/0"+str(mes))
                elif len(str(dia)) == 1 and len(str(mes)) > 1:
                    print("0"+str(dia)+"/"+str(mes))
                else:
                    print(str(dia)+"/"+str(mes))
                dia += 1
            dia = 1    
        else:
            while dia <= 30:
                if len(str(dia)) == 1 and len(str(mes)) == 1:
                    print ("0"+str(dia)+"/0"+str(mes))
                elif len(str(dia)) > 1  and len(str(mes)) == 1:
                    print(str(dia)+"/0"+str(mes))
                elif len(str(dia)) == 1 and len(str(mes)) > 1:
                    print("0"+str(dia)+"/"+str(mes))
                else:
                    print(str(dia)+"/"+str(mes))
                dia += 1
            dia = 1
    mes += 1         
    
    
