import os

# 1️ Criar uma lista de dados
dados = ["banana", "maçã", "laranja", "uva", "melancia"]

# 2️ Definir o nome da pasta e do arquivo
nome_pasta = "meus_dados"
nome_arquivo = "frutas.txt"

# 3️ Verificar se a pasta já existe; se não, criar
if not os.path.exists(nome_pasta):
    os.mkdir(nome_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso!")
else:
    print(f"A pasta '{nome_pasta}' já existe.")

# 4 Gerar o caminho completo do arquivo
caminho_arquivo = os.path.join(nome_pasta, nome_arquivo)

# 5️ Criar o arquivo de texto e escrever os dados dentro dele
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for item in dados:
        arquivo.write(item + "\n")

print(f"\n Arquivo '{nome_arquivo}' criado e salvo dentro da pasta '{nome_pasta}'!")

# 6️ Mostrar o diretório atual do script
print("\n Diretório atual:", os.getcwd())

# 7️ (Opcional) Listar o conteúdo da pasta criada
print("\n Conteúdo da pasta criada:")
for item in os.listdir(nome_pasta):
    print("-", item)
