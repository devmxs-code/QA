import os
# Criar uma lista de dados do sistema operacional


# Mostra o diretório atual
print("Diretório atual:", os.getcwd())

# Cria uma nova pasta (se não existir)
if not os.path.exists("nova_pasta"):
    os.mkdir("nova_pasta")
    print("Pasta 'nova_pasta' criada com sucesso!")
else:
    print("A pasta já existe.")

# Lista arquivos e pastas do diretório atual
print("\nConteúdo da pasta atual:")
for item in os.listdir():
    print("-", item)
