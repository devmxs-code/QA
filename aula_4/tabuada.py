# Solicita um valor ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Estrutura de repetição para gerar a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
