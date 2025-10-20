# especificacao do aluno
nome = input("Olá! Qual é o seu nome? ")

# coletando as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# calculo media do aluno
media = (nota1 + nota2 + nota3 + nota4) / 4

# retorno
print(f"Olá, {nome}! Sua média é: {media:.1f} pontos.")