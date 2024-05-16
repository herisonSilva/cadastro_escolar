import mySQLconection
codigo = 11
while codigo !=0:
    mySQLconection.lista_de_comandos()
    codigo = int(input('escolha uma opção. '))
    if codigo == 1:
        nome = input('Qual o nome do aluno. ')
        matricula = int(input(f'Qual o número da matricula do aluno: {nome}. '))
        curso = input(f"Qual o curso que o aluno {nome} irá cursar. ")
        mySQLconection.insert(nome, matricula, curso)
        print(f'novo aluno cadastrado com sucesso. ')
    elif codigo == 2:
        nome = input('digite o nome do aluno que vc dejesa editar. ')
        curso = input(f'digite o novo curso do aluno {nome}. ')
        mySQLconection.update(curso, nome)
        print('atualizado com suceso. ')
    elif codigo == 3:
        print(mySQLconection.exibir())
    elif codigo == 4:
        nome = input('digite o nome do aluno que você deseja excluir. ')
        mySQLconection.delete(nome)
        print(f'{nome} Exluido com sucesso. ')
    else:
        print('digite um código válido. ')
