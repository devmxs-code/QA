# Lista de frutas disponíveis
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Lista de alergias (inicialmente vazia)
alergias = []

# Mostra as frutas disponíveis
print("Lista de frutas disponíveis:", frutas)

# Solicita ao usuário uma fruta que causa alergia
fruta_alergia = input("Digite o nome de uma fruta que você tem alergia: ").lower()

# Adiciona a fruta informada à lista de alergias
alergias.append(fruta_alergia)

# Estrutura de repetição e condicional
for fruta in frutas:
    if fruta in alergias:
        print(f"Atenção! Você é alérgico(a) a {fruta}.")
