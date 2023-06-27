nome = "Ricardo"
sobrenome = "Araújo"
idade = 34
ano_de_nascimento = 1988
maior_de_idade = idade >= 18
altura = 1.63
peso = 67
imc = peso / altura ** 2

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_de_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura em metros:", altura)
print(f"Seu IMC é {imc:.2f}")
print()