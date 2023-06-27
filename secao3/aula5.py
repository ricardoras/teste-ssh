"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Por favor digite seu nome! ')
idade = input('Por favor digite sua idade! ')
numero_caracteres = len(nome)

if nome and idade:
    print(f'\nSeu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome tem espaços.')
    else:
        print('Seu nome não contém espaços.')
    print(f'O nome que você digitou possui {numero_caracteres} letras') 
    print(f'Sua idade é {idade}')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome)-1]}')
else:
    print('Desculpe, você deixou campos vazios.')