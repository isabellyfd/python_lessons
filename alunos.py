alunos = []
disciplinas = []

def cadastroAluno():
    cpf = input("Digite o cpf\n")
    nome =  input("Digite o nome\n")
    aluno = {
            "cpf": cpf,
            "nome": nome,
            "disc": {}
        }
    alunos.append(aluno)

def verificaAluno(cpf):
    for x in alunos:
        if x["cpf"] == cpf:
            return x
    return {}
    
def verificaDisc(cod):
    for x in disciplinas:
        if x["cod"] == cpf:
            return x
    return {}
    
def removerAluno(cpf):
    indice = 0
    for x in alunos:
        if x["cpf"] == cpf:
            del alunos[indice]
        indice += 1

def cadastroDisciplina():
    cod = input("Digite o codigo\n")
    nome =  input("Digite o nome\n")
    disc = {
            "cod": cod,
            "nome": nome,
        }
    disciplinas.append(disc)    
    
    
def verificar():
    cpf = input("Digite o cpf do aluno\n")
    cod  = input("Digite o codigo da cisciplina\n")
    if verificarAluno(cpf) != {}:
        if verificarDisc(cod) != {}:
            result = verificarAluno(cpf)
            result[""]
    else:
        print("Esse Aluno não existe")     
    
        
print("Voce deseja fazer:\n1-Cadastrar Aluno\n2-Verificar Aluno\n3-Remover Aluno\n4-Cadastrar Disciplina\n5-Verificar (Aluno -> Disciplina)\n6-Sair")
entrada  =  input()
while entrada != "6":
    if entrada == "1":
        cadastrarAluno()
    elif entrada == "2":
        cpf = input("Digite o cpf do aluno")
        if verificarAluno(cpf) != {}:
            result = verificarAluno(cpf)
            print("O Aluno", result["nome"], "de cpf", result["cpf"], "ja esta cadastrado\n")
        else:
            print("Esse Aluno nao existe")
    elif entrada == "3":
        cpf = input("Digite o cpf do aluno que deseja remover\n")
        if verificarAluno(cpf) == {}:
            print ("Esse Aluno nao existe)
        else:
            removerAluno(cpf)
    elif entrada == "4":
        cadastrarDisciplina()
    elif  entrada == "5":
                
            

