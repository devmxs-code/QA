from faker import Faker
import csv

# inicializa o faker em português do brasil
fake = Faker("pt_BR")

def criar_persona_lista(qtd=10):
    # cria uma lista vazia para armazenar as personas
    persona_lista = []
    
    # repete o processo de criação de personas pela quantidade informada
    for _ in range(qtd):
        # gera um nome fictício
        nome = fake.name()
        
        # gera uma data de nascimento aleatória entre 18 e 65 anos
        nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
        
        # calcula a idade aproximada com base no ano atual (2025)
        idade = 2025 - nascimento.year
        
        # gera o nome de uma cidade fictícia
        cidade = fake.city()
        
        # adiciona os dados da persona à lista como um dicionário
        persona_lista.append({
            "Nome": nome,
            "Data de Nascimento": nascimento.strftime("%d/%m/%Y"),
            "Idade": idade,
            "Cidade": cidade
        })
    
    # retorna a lista completa de personas geradas
    return persona_lista


def salvar_csv(nome_arquivo="personas.csv", qtd=10):
    # cria a lista de personas com base na quantidade desejada
    personas = criar_persona_lista(qtd)

    # cria e escreve o arquivo csv
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
        # define os campos (colunas) do arquivo csv
        campos = ["Nome", "Data de Nascimento", "Idade", "Cidade"]
        
        # cria um escritor de csv baseado em dicionários
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        
        # escreve o cabeçalho no arquivo
        escritor.writeheader()
        
        # escreve todas as linhas (cada persona) no arquivo
        escritor.writerows(personas)

    # exibe mensagem confirmando a criação do arquivo
    print(f"arquivo '{nome_arquivo}' criado com {qtd} personas!")


# gerar personas e salva no arquivo personas.csv
salvar_csv("personas.csv", 20000)