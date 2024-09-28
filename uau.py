def situacao ( media, frequencia):
    if frequencia<75:
        return 'Reprovado por FALTA'
    elif media < 7:
        return 'Reprovado por MEDIA'
    else: 
        return 'Aprovado'
dados={}
n = -1
while n != 5:
    print('---------- SISTEMA ACADÊMICO ----------')
    print('''Informe uma ação:
    1- Adicionar aluno 
    2- Editar informações de nome do aluno
    3 - Remover aluno existente
    4 - Relatório de situação dos alunos
    5 - Sair
      ''')
    n=int(input('-> '))
    if n == 1:
        name=str(input('Digite o nome: ')).strip().capitalize()
        if name in dados:
            print ('Aluno já existe!')
        else:
            frequencia=int(input('Qual a frequência desse aluno? '))
            c=1
            a=0
            while c <=4:
                note=float(input(f'Digite a nota da N{c}: '))
                c+=1
                a+=note
            media=a/4
            resultado=situacao(media,frequencia)
            dados[name]=[media,frequencia,resultado]
            print ('Aluno adicionado!')
    if n == 2:
        print('Qual aluno deseja editar?')
        print(dados.keys())
        edit=str(input('Digite aqui: ')).strip().capitalize()
        if edit in dados.keys():
            nome=str(input('Digite um novo nome:')).strip().capitalize()
            dados[nome]= dados.pop(edit)
            print('Editado com sucesso!')
        else:
            print('Aluno inexistente')
    if n==3:
        print('Qual aluno deseja remover?')
        print(dados.keys())
        rem=str(input('Digite aqui: ')).strip().capitalize()
        if rem in dados.keys():
            del dados[rem]
            print('Aluno removido!')
        else:
            print('Aluno não encontrado')
    if n==4:
        for name in dados:
            print(f'O aluno {name} possui media {dados[name][0]} frequência de {dados[name][1]} aulas e está {dados[name][2]}')

    if n==5:
        break